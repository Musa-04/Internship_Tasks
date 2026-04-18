import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/telco_churn_clean.csv")

sns.set_theme(style="whitegrid")

# ── Plot 1: Churn Distribution ──────────────────────────────────────────
plt.figure(figsize=(5, 4))
ax = sns.countplot(x='Churn', data=df, palette=['#2ecc71', '#e74c3c'])
ax.set_xticklabels(['No Churn (0)', 'Churn (1)'])
plt.title('Churn Distribution')
plt.ylabel('Count')
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2, p.get_height() + 30),
                ha='center', fontsize=11)
plt.tight_layout()
plt.savefig("data/plot1_churn_distribution.png")
plt.show()
print("Plot 1 saved!")

# ── Plot 2: Churn by Gender ──────────────────────────────────────────────
plt.figure(figsize=(6, 4))
sns.countplot(x='gender', hue='Churn', data=df, palette=['#2ecc71', '#e74c3c'])
plt.title('Churn by Gender')
plt.legend(labels=['No Churn', 'Churn'])
plt.tight_layout()
plt.savefig("data/plot2_churn_by_gender.png")
plt.show()
print("Plot 2 saved!")

# ── Plot 3: Churn by Contract Type ──────────────────────────────────────
plt.figure(figsize=(7, 4))
sns.countplot(x='Contract', hue='Churn', data=df, palette=['#2ecc71', '#e74c3c'])
plt.title('Churn by Contract Type')
plt.legend(labels=['No Churn', 'Churn'])
plt.tight_layout()
plt.savefig("data/plot3_churn_by_contract.png")
plt.show()
print("Plot 3 saved!")

# ── Plot 4: Churn by Internet Service ───────────────────────────────────
plt.figure(figsize=(7, 4))
sns.countplot(x='InternetService', hue='Churn', data=df, palette=['#2ecc71', '#e74c3c'])
plt.title('Churn by Internet Service')
plt.legend(labels=['No Churn', 'Churn'])
plt.tight_layout()
plt.savefig("data/plot4_churn_by_internet.png")
plt.show()
print("Plot 4 saved!")

# ── Plot 5: Monthly Charges Distribution ────────────────────────────────
plt.figure(figsize=(7, 4))
sns.histplot(data=df, x='MonthlyCharges', hue='Churn', bins=40,
             palette=['#2ecc71', '#e74c3c'], kde=True)
plt.title('Monthly Charges vs Churn')
plt.tight_layout()
plt.savefig("data/plot5_monthly_charges.png")
plt.show()
print("Plot 5 saved!")

# ── Plot 6: Tenure Distribution ─────────────────────────────────────────
plt.figure(figsize=(7, 4))
sns.histplot(data=df, x='tenure', hue='Churn', bins=40,
             palette=['#2ecc71', '#e74c3c'], kde=True)
plt.title('Tenure vs Churn')
plt.tight_layout()
plt.savefig("data/plot6_tenure.png")
plt.show()
print("Plot 6 saved!")

# ── Plot 7: Correlation Heatmap ─────────────────────────────────────────
plt.figure(figsize=(8, 6))
numeric_df = df.select_dtypes(include='number')
sns.heatmap(numeric_df.corr(), annot=True, fmt=".2f", cmap='RdYlGn', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.savefig("data/plot7_correlation_heatmap.png")
plt.show()
print("Plot 7 saved!")

print("\n✅ All EDA plots saved in the data/ folder!")