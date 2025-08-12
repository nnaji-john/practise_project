"""
Mid-Term Assignment
July 27, 2025
Johnpaul Nnaji
"""


# Load required libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency

# Load dataset
df = pd.read_csv('StudentsPerformance.csv')

# -----------------------------------------------------
# PART 1: Frequency Distribution – Math Score
# -----------------------------------------------------
print("== Frequency Distribution: Math Score ==")

# Define bins and labels
bins = [0, 59, 69, 79, 89, 100]
labels = ['0–59', '60–69', '70–79', '80–89', '90–100']
df['math_score_bin'] = pd.cut(df['math score'], bins=bins, labels=labels, include_lowest=True)

# Frequency table
math_freq_dist = df['math_score_bin'].value_counts().sort_index()
print(math_freq_dist, "\n")

# -----------------------------------------------------
# PART 2: Summary Statistics – Math Score
# -----------------------------------------------------
print("== Summary Statistics: Math Score ==")

math_mean = df['math score'].mean()
math_median = df['math score'].median()
math_mode = df['math score'].mode()[0]
math_range = df['math score'].max() - df['math score'].min()
math_variance = df['math score'].var()
math_std = df['math score'].std()

print(f"Mean: {math_mean:.2f}")
print(f"Median: {math_median}")
print(f"Mode: {math_mode}")
print(f"Range: {math_range}")
print(f"Variance: {math_variance:.2f}")
print(f"Standard Deviation: {math_std:.2f}\n")

# -----------------------------------------------------
# PART 3: Association – Gender vs Lunch
# -----------------------------------------------------
print("== Contingency Table: Gender vs Lunch Type ==")
contingency_table = pd.crosstab(df['gender'], df['lunch'])
print(contingency_table, "\n")

# Chi-square test
chi2_stat, p_value, dof, expected = chi2_contingency(contingency_table)

# Cramér’s V
n = contingency_table.to_numpy().sum()
cramers_v = np.sqrt(chi2_stat / (n * (min(contingency_table.shape) - 1)))

print("Chi-square Test Results:")
print(f"Chi-square statistic: {chi2_stat:.4f}")
print(f"p-value: {p_value:.4f}")
print(f"Degrees of freedom: {dof}")
print(f"Cramér’s V: {cramers_v:.4f}\n")

# -----------------------------------------------------
# PART 4: Correlation – Math vs Reading
# -----------------------------------------------------
print("== Correlation: Math vs Reading Score ==")
correlation = df[['math score', 'reading score']].corr().iloc[0, 1]
print(f"Pearson Correlation Coefficient (r): {correlation:.3f}\n")

# -----------------------------------------------------
# Scatter Plot
# -----------------------------------------------------
plt.figure(figsize=(8, 6))
sns.scatterplot(x='math score', y='reading score', data=df)
plt.title('Scatter Plot: Math Score vs Reading Score')
plt.xlabel('Math Score')
plt.ylabel('Reading Score')
plt.grid(True)
plt.tight_layout()
plt.savefig('Figure1_Math_vs_Reading.png')  # Save figure for report
plt.show()


