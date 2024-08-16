#Ilakiya Emily J
#August 2024
"""Removal of columns such as ‘Lower bound’ and ‘Upper bound’ that are irrelevant
Renaming ‘Area’ as ‘Location’ and ‘M/F’ as ‘Sex’ to improves clarity
Exclusion of rows where ‘Measure’ is ‘Affected rank’ ensures it's only analyzing the actual rates of the affected individuals without including rankings or other irrelevant metrics.
Number of Rows: 14259
Number of Columns: 8
Columns: Location, Area,Age,M/F,Cause of death or injury,Measure,Value per 100,000,Lower bound,Upper bound"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('/content/drive/MyDrive/final data sheet.csv')
"""Rename Values
Coloumns heads renamed for clarity."""
data.rename(columns={
    'Area': 'Location',
    'M/F': 'Sex',
    'Cause of death or injury': 'Disease'
}, inplace=True)
"""
Dropping Unwanted Columns like lower bound and upper bound since they are not needed for the analysis"""
columns_to_drop = ['Lower bound', 'Upper bound']
data_cleaned = data.drop(columns=columns_to_drop)
""" Removing rows that have rank and other irrelevant metrics."""
data_filtered = data_cleaned[data_cleaned['Measure'].str.lower() != 'affected rank']
# Define custom colors for each disease
colors = {
    'Cardiovascular diseases': '#ff9999',
    'Chronic respiratory diseases': '#66b3ff',
    'Diabetes and kidney diseases': '#99ff99',
    'Digestive diseases': '#ffcc99',
    'Enteric infections': '#c2c2f0',
    'HIV/AIDS and sexually transmitted infections': '#ffb3e6',
    'Maternal and neonatal disorders': '#c2f0c2',
    'Mental disorders': '#f0c2c2',
    'Musculoskeletal disorders': '#f0c2e2',
    'Neglected tropical diseases and malaria': '#d2b4de',
    'Neoplasms': '#9b59b6',
    'Neurological disorders': '#3498db',
    'Nutritional deficiencies': '#e74c3c',
    'Other COVID-19 pandemic-related outcomes': '#34495e',
    'Other infectious diseases': '#f39c12',
    'Other non-communicable diseases': '#2ecc71',
    'Respiratory infections and tuberculosis': '#1abc9c',
    'Self-harm and interpersonal violence': '#16a085',
    'Sense organ diseases': '#f1c40f',
    'Skin and subcutaneous diseases': '#e67e22',
    'Substance use disorders': '#e74c3c',
    'Transport injuries': '#34495e',
    'Unintentional injuries': '#8e44ad'
}

print(data_filtered.head())
print(data_filtered.info())

# Displaying the first few rows of the cleaned data.
print(data.head())
print(data.info())
print(data['Location'].value_counts())
print(data['Disease'].value_counts())
plt.figure(figsize=(10, 6))
data_filtered['Value per 100,000'].hist(bins=50)
plt.title('Distribution of Value per 100,000')
plt.xlabel('Value per 100,000')
plt.ylabel('Frequency')
plt.show()
summary_statistics = data_filtered.describe()
print(summary_statistics)

disease_totals = data_filtered.groupby(['Location', 'Disease'])['Value per 100,000'].sum().unstack()
disease_colors = [colors[disease] for disease in disease_totals.columns if disease in colors]
#Histogram: Distribution of 'Value per 100,000'
plt.figure(figsize=(10, 6))
sns.histplot(data_filtered['Value per 100,000'], bins=50, kde=True)
plt.title('Distribution of Value per 100,000')
plt.xlabel('Value per 100,000')
plt.ylabel('Frequency')
plt.show()
#Stacked barchart: Distribution of Diseases by State
disease_totals.plot(kind='bar', stacked=True, figsize=(14, 8), color=disease_colors)
plt.title('Stacked Bar Chart of Disease Distribution by State')
plt.xlabel('State')
plt.ylabel('Total Value per 100,000')
plt.legend(title='Disease', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()
#Compare Disease Prevalence and Age Demographics Across States:Heatmap
grouped_data = data_filtered.groupby(['Location', 'Age'])['Value per 100,000'].mean().unstack()
plt.figure(figsize=(12, 8))
sns.heatmap(grouped_data, annot=True, fmt=".2f", cmap='YlGnBu')
plt.title('Average Disease Prevalence by Age and State')
plt.xlabel('Age Group')
plt.ylabel('State')
plt.show()
# Correlation Analysis using Pandas
#Scatterplot
plt.figure(figsize=(10, 6))
sns.scatterplot(
    x='Age',
    y='Value per 100,000',
    hue='Disease',
    data=data_filtered,
    palette=colors,
    alpha=0.7
)
plt.title('Correlation between Age and Disease Incidence')
plt.xlabel('Age')
plt.ylabel('Value per 100,000')
plt.legend(title='Disease', loc='center left', bbox_to_anchor=(1, 0.5))
plt.grid(True)
plt.show()
