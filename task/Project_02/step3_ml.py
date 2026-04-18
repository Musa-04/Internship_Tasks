import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (accuracy_score, classification_report,
                             confusion_matrix, roc_auc_score, roc_curve)
from xgboost import XGBClassifier
import warnings
warnings.filterwarnings('ignore')

# ── 1. Load Data ─────────────────────────────────────────────────────────
df = pd.read_csv("data/telco_churn_clean.csv")

# ── 2. Encode Categorical Columns ────────────────────────────────────────
le = LabelEncoder()
cat_cols = df.select_dtypes(include='object').columns
for col in cat_cols:
    df[col] = le.fit_transform(df[col])

# ── 3. Split Features & Target ───────────────────────────────────────────
X = df.drop('Churn', axis=1)
y = df['Churn']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

# ── 4. Scale Features ────────────────────────────────────────────────────
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test  = scaler.transform(X_test)

# ── 5. Train 3 Models ────────────────────────────────────────────────────
models = {
    "Logistic Regression": LogisticRegression(random_state=42),
    "Random Forest":       RandomForestClassifier(n_estimators=100, random_state=42),
    "XGBoost":             XGBClassifier(use_label_encoder=False,
                                         eval_metric='logloss', random_state=42)
}

results = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]
    results[name] = {
        "model":    model,
        "accuracy": accuracy_score(y_test, y_pred),
        "roc_auc":  roc_auc_score(y_test, y_prob),
        "y_pred":   y_pred,
        "y_prob":   y_prob
    }
    print(f"\n{'='*45}")
    print(f" {name}")
    print(f"{'='*45}")
    print(f" Accuracy : {accuracy_score(y_test, y_pred):.4f}")
    print(f" ROC-AUC  : {roc_auc_score(y_test, y_prob):.4f}")
    print(classification_report(y_test, y_pred, target_names=["No Churn","Churn"]))

# ── 6. Plot: Model Comparison ────────────────────────────────────────────
names     = list(results.keys())
accuracy  = [results[n]["accuracy"] for n in names]
roc_aucs  = [results[n]["roc_auc"]  for n in names]

x = np.arange(len(names))
fig, ax = plt.subplots(figsize=(8, 5))
bars1 = ax.bar(x - 0.2, accuracy, 0.35, label='Accuracy',  color='#3498db')
bars2 = ax.bar(x + 0.2, roc_aucs, 0.35, label='ROC-AUC',   color='#e74c3c')
ax.set_xticks(x)
ax.set_xticklabels(names)
ax.set_ylim(0.5, 1.0)
ax.set_title('Model Comparison')
ax.legend()
for bar in bars1 + bars2:
    ax.text(bar.get_x() + bar.get_width()/2,
            bar.get_height() + 0.005,
            f'{bar.get_height():.3f}', ha='center', fontsize=9)
plt.tight_layout()
plt.savefig("data/plot8_model_comparison.png")
plt.show()
print("Plot 8 saved!")

# ── 7. Plot: Confusion Matrices ──────────────────────────────────────────
fig, axes = plt.subplots(1, 3, figsize=(15, 4))
for ax, (name, res) in zip(axes, results.items()):
    cm = confusion_matrix(y_test, res["y_pred"])
    sns.heatmap(cm, annot=True, fmt='d', ax=ax,
                cmap='Blues', cbar=False,
                xticklabels=['No Churn','Churn'],
                yticklabels=['No Churn','Churn'])
    ax.set_title(name)
    ax.set_xlabel('Predicted')
    ax.set_ylabel('Actual')
plt.tight_layout()
plt.savefig("data/plot9_confusion_matrices.png")
plt.show()
print("Plot 9 saved!")

# ── 8. Plot: ROC Curves ──────────────────────────────────────────────────
plt.figure(figsize=(7, 5))
colors = ['#3498db', '#2ecc71', '#e74c3c']
for (name, res), color in zip(results.items(), colors):
    fpr, tpr, _ = roc_curve(y_test, res["y_prob"])
    plt.plot(fpr, tpr, label=f'{name} (AUC={res["roc_auc"]:.3f})', color=color)
plt.plot([0,1],[0,1],'k--', linewidth=0.8)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curves — All Models')
plt.legend()
plt.tight_layout()
plt.savefig("data/plot10_roc_curves.png")
plt.show()
print("Plot 10 saved!")

# ── 9. Feature Importance (XGBoost) ─────────────────────────────────────
xgb_model = results["XGBoost"]["model"]
feat_imp = pd.Series(xgb_model.feature_importances_,
                     index=df.drop('Churn', axis=1).columns)
feat_imp = feat_imp.sort_values(ascending=False).head(10)

plt.figure(figsize=(8, 5))
sns.barplot(x=feat_imp.values, y=feat_imp.index, palette='viridis')
plt.title('Top 10 Feature Importances (XGBoost)')
plt.xlabel('Importance Score')
plt.tight_layout()
plt.savefig("data/plot11_feature_importance.png")
plt.show()
print("Plot 11 saved!")

# ── 10. Save Best Model ──────────────────────────────────────────────────
import joblib, os
os.makedirs("model", exist_ok=True)

best_name  = max(results, key=lambda n: results[n]["roc_auc"])
best_model = results[best_name]["model"]
joblib.dump(best_model, "model/best_model.pkl")
joblib.dump(scaler,     "model/scaler.pkl")

# Save feature names
feature_names = df.drop('Churn', axis=1).columns.tolist()
joblib.dump(feature_names, "model/feature_names.pkl")

print(f"\n✅ Best model: {best_name}")
print(f"✅ Model saved to model/best_model.pkl")
print(f"✅ Scaler saved to model/scaler.pkl")