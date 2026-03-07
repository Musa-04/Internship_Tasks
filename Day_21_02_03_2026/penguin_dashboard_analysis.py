import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=sns.load_dataset("penguins")

print("\nOriginal Dataset Shape:", df.shape)

df=df.dropna()
df.reset_index(drop=True,inplace=True)
print("Clean DataSet Shape:",df.shape)

print("----KPI Section-----")
#1
total_penguins=df.shape[0]
print("Total Penguins:",total_penguins)

#2
species_count=df['species'].value_counts()
species_percent=df['species'].value_counts(normalize=True)*100

print("\nSpecies Count")
print(species_count)

print("\nSpecies Percentage")
print(species_percent)

# 3 Island-wise Population
island_count = df['island'].value_counts()
island_percent = df['island'].value_counts(normalize=True) * 100


print("\nIsland Population")
print(island_count)

print("\nIsland Percentage")
print(island_percent)

print("-------Biological Measurements KPR------")
# 4 Average Body Mass
print("\nAverage Body Mass Overall:", df['body_mass_g'].mean())

print("\nAverage Body Mass by Species")
print(df.groupby('species')['body_mass_g'].mean())

print("\nAverage Body Mass by Gender")
print(df.groupby('sex')['body_mass_g'].mean())

#5 Average Flipper Length
print("\nAverage Flipper Length Overall:", df['flipper_length_mm'].mean())

print("\nAverage Flipper Length by Species")
print(df.groupby('species')['flipper_length_mm'].mean())

print("\nAverage Flipper Length by Gender")
print(df.groupby('sex')['flipper_length_mm'].mean())

# 6 Average Bill Length
print("\nAverage Bill Length Overall:", df['bill_length_mm'].mean())

print("\nAverage Bill Length by Species")
print(df.groupby('species')['bill_length_mm'].mean())


# 7 Average Bill Depth
print("\nAverage Bill Depth Overall:", df['bill_depth_mm'].mean())

print("\nAverage Bill Depth by Species")
print(df.groupby('species')['bill_depth_mm'].mean())


# 8 Bill Ratio KPI
df["bill_ratio"] = df["bill_length_mm"] / df["bill_depth_mm"]

print("\nAverage Bill Ratio by Species")
print(df.groupby("species")["bill_ratio"].mean())


print("\n========= GENDER KPIs =========")

# 9 Male vs Female
gender_count = df["sex"].value_counts()
gender_percent = df["sex"].value_counts(normalize=True) * 100

print("\nGender Count")
print(gender_count)

print("\nGender Percentage")
print(gender_percent)


# 10 Size Difference by Gender
mass_gender = df.groupby("sex")["body_mass_g"].mean()
flipper_gender = df.groupby("sex")["flipper_length_mm"].mean()

print("\nBody Mass Difference (Male-Female):",
      mass_gender["Male"] - mass_gender["Female"])

print("Flipper Length Difference (Male-Female):",
      flipper_gender["Male"] - flipper_gender["Female"])

print("\n======= CORRECLATION KPIS ======")

corr_matrix=df[[
    "body_mass_g",
    "flipper_length_mm",
    "bill_length_mm",
    "bill_depth_mm"
]].corr()

print("\nCorrelation Matrix")
print(corr_matrix)


# Highest correlation pair
corr_pairs = corr_matrix.unstack()
sorted_corr = corr_pairs.sort_values(ascending=False)

print("\nHighest Correlation Pairs")
print(sorted_corr[1:6])

print("\n========= ISLAND KPIs =========")

# 13 Species per island
species_island = pd.crosstab(df["island"], df["species"])

print("\nSpecies per Island")
print(species_island)


# 14 Average Body Mass per Island
print("\nAverage Body Mass per Island")
print(df.groupby("island")["body_mass_g"].mean())


# 15 Average Flipper Length per Island
print("\nAverage Flipper Length per Island")
print(df.groupby("island")["flipper_length_mm"].mean())

print("\n========= DATA QUALITY =========")

missing_percent = df.isnull().sum() / len(df) * 100

print("\nMissing Value Percentage")
print(missing_percent)

plt.figure(figsize=(14,10))

#1 Species Distribution
plt.subplot(3,3,1)
sns.countplot(data=df,x="species")
plt.title("Species Distribution")

# 2 Island Distribution
plt.subplot(3,3,2)
sns.countplot(data=df, x="island")
plt.title("Island Distribution")


# 3 Gender Distribution
plt.subplot(3,3,3)
df["sex"].value_counts().plot.pie(autopct="%1.1f%%")
plt.title("Gender Distribution")
plt.ylabel("")


# 4 Body Mass Histogram
plt.subplot(3,3,4)
sns.histplot(df["body_mass_g"], bins=20)
plt.title("Body Mass Distribution")


# 5 Flipper Length Histogram
plt.subplot(3,3,5)
sns.histplot(df["flipper_length_mm"], bins=20)
plt.title("Flipper Length Distribution")


# 6 Bill Length Histogram
plt.subplot(3,3,6)
sns.histplot(df["bill_length_mm"], bins=20)
plt.title("Bill Length Distribution")


# 7 Average Body Mass by Species
plt.subplot(3,3,7)
sns.barplot(data=df, x="species", y="body_mass_g")
plt.title("Avg Body Mass by Species")


# 8 Average Flipper Length by Species
plt.subplot(3,3,8)
sns.barplot(data=df, x="species", y="flipper_length_mm")
plt.title("Avg Flipper Length by Species")


# 9 Avg Body Mass by Gender
plt.subplot(3,3,9)
sns.barplot(data=df, x="sex", y="body_mass_g")
plt.title("Avg Body Mass by Gender")

plt.tight_layout()
plt.show()


# ================================
# RELATIONSHIP CHARTS
# ================================

# Scatter Plot
plt.figure(figsize=(6,5))
sns.scatterplot(
    data=df,
    x="flipper_length_mm",
    y="body_mass_g",
    hue="species"
)
plt.title("Flipper Length vs Body Mass")
plt.show()


# Bill Length vs Bill Depth
plt.figure(figsize=(6,5))
sns.scatterplot(
    data=df,
    x="bill_length_mm",
    y="bill_depth_mm",
    hue="species"
)
plt.title("Bill Length vs Bill Depth")
plt.show()


# Correlation Heatmap
plt.figure(figsize=(6,5))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()