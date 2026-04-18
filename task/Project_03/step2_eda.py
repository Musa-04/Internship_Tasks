import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

df = pd.read_csv("data/ecommerce_clean.csv")
sns.set_theme(style="whitegrid")
os.makedirs("data/plots", exist_ok=True)

# ── Plot 1: Sales by Category ─────────────────────────────────────────────
plt.figure(figsize=(8, 4))
cat_sales = df.groupby('Category')['TotalAmount'].sum().sort_values(ascending=False)
sns.barplot(x=cat_sales.index, y=cat_sales.values, palette='viridis')
plt.title('Total Sales by Category')
plt.ylabel('Total Amount (₹)')
plt.xlabel('Category')
plt.tight_layout()
plt.savefig("data/plots/plot1_sales_by_category.png")
plt.show()
print("Plot 1 saved!")

# ── Plot 2: Top 10 Products by Revenue ───────────────────────────────────
plt.figure(figsize=(9, 4))
top_products = df.groupby('Product')['TotalAmount'].sum().sort_values(ascending=False).head(10)
sns.barplot(x=top_products.values, y=top_products.index, palette='magma')
plt.title('Top 10 Products by Revenue')
plt.xlabel('Total Amount (₹)')
plt.tight_layout()
plt.savefig("data/plots/plot2_top_products.png")
plt.show()
print("Plot 2 saved!")

# ── Plot 3: Rating Distribution ───────────────────────────────────────────
plt.figure(figsize=(6, 4))
sns.countplot(x='Rating', data=df, palette='coolwarm')
plt.title('Rating Distribution')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig("data/plots/plot3_rating_distribution.png")
plt.show()
print("Plot 3 saved!")

# ── Plot 4: Sales by City ─────────────────────────────────────────────────
plt.figure(figsize=(8, 4))
city_sales = df.groupby('City')['TotalAmount'].sum().sort_values(ascending=False)
sns.barplot(x=city_sales.index, y=city_sales.values, palette='Set2')
plt.title('Total Sales by City')
plt.ylabel('Total Amount (₹)')
plt.tight_layout()
plt.savefig("data/plots/plot4_sales_by_city.png")
plt.show()
print("Plot 4 saved!")

# ── Plot 5: Payment Method Distribution ──────────────────────────────────
plt.figure(figsize=(6, 4))
df['PaymentMethod'].value_counts().plot.pie(autopct='%1.1f%%',
    colors=['#3498db','#2ecc71','#e74c3c','#f39c12'], startangle=90)
plt.title('Payment Method Distribution')
plt.ylabel('')
plt.tight_layout()
plt.savefig("data/plots/plot5_payment_methods.png")
plt.show()
print("Plot 5 saved!")

# ── Plot 6: Monthly Sales Trend ───────────────────────────────────────────
plt.figure(figsize=(10, 4))
monthly = df.groupby('Month')['TotalAmount'].sum()
sns.lineplot(x=monthly.index, y=monthly.values, marker='o', color='#3498db')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Amount (₹)')
plt.xticks(range(1, 13))
plt.tight_layout()
plt.savefig("data/plots/plot6_monthly_trend.png")
plt.show()
print("Plot 6 saved!")

# ── Plot 7: Sales by Day of Week ──────────────────────────────────────────
plt.figure(figsize=(8, 4))
days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
day_sales = df.groupby('DayOfWeek')['TotalAmount'].sum()
sns.barplot(x=[days[i] for i in day_sales.index], y=day_sales.values, palette='Blues_d')
plt.title('Sales by Day of Week')
plt.ylabel('Total Amount (₹)')
plt.tight_layout()
plt.savefig("data/plots/plot7_sales_by_day.png")
plt.show()
print("Plot 7 saved!")

# ── Plot 8: Correlation Heatmap ───────────────────────────────────────────
plt.figure(figsize=(7, 5))
numeric_df = df.select_dtypes(include='number')
sns.heatmap(numeric_df.corr(), annot=True, fmt=".2f", cmap='RdYlGn', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.savefig("data/plots/plot8_correlation.png")
plt.show()
print("Plot 8 saved!")

print("\n✅ All 8 EDA plots saved in data/plots/ folder!")