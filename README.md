Data Overview:
Removing columns like 'Lower bound' and 'Upper bound' that are not relevant for the analysis
Renaming 'Area' to 'Location' and 'M/F' to 'Sex' aligns with common terminology and improves clarity.
Removing rows where 'Measure' is 'affected rank' ensuring that it is only analyzing the actual rates of affected individuals, not rankings or other irrelevant metrics
Number of Rows: 14259
Number of Columns: 8
Columns: Location, Area, Age, M/F, Cause of death or injury, Measure, Value per 100,000, Lower bound, Upper bound
Data Cleaning and Preparation:
1.	Columns Removed:
'Lower bound'
'Upper bound'
2.	Columns Renamed:
'Area' to 'Location'
'M/F' to 'Sex'
'Cause of death or injury' to 'Disease'
3.	Rows Filtered:
Excluded rows where Measure was 'Affected rank'.
Key Findings:
1.	Distribution Analysis:
o	Value per 100,000: The distribution of disease incidence shows a range of values with some outliers.
o	Histogram and summary statistics reveal a right-skewed distribution, indicating higher values are less common but significant.
2.	Disease Distribution by State:
  This stacked bar chart shows the distribution of various diseases across different Indian states.
    The x-axis represents different states, while the y-axis shows the total value per 100,000 of the population.
    Each colour in the bars corresponds to a specific disease, as indicated in the legend on the right side.
  Uttar Pradesh shows the highest total disease burden, with a diverse range of diseases contributing to the total value.
  States like Bihar, Maharashtra, and Madhya Pradesh also show significant disease burdens.
  The chart effectively visualizes how disease prevalence varies significantly across states, highlighting regional health disparities.
3.Age group analysis:
  This heatmap presents the average disease prevalence across different age groups for each state.
The x-axis represents age groups, while the y-axis represents different states.
 Darker shades indicate higher disease prevalence in the respective age groups.
 Uttar Pradesh, Maharashtra, and Bihar exhibit the highest disease prevalence,     especially in the older age groups (50-69 years and 70+ years).
The heatmap clearly shows that disease prevalence generally increases with age, particularly in the older populations.    
4. Correlation Analysis:
  This scatterplot displays the correlation between age and disease incidence across different diseases.
  The x-axis represents different age groups, while the y-axis represents the disease incidence value per 100,000.
  Each point represents a specific disease's incidence in a given age group.
  The scatterplot shows a clear trend where disease incidence increases with age, especially for chronic conditions like cardiovascular diseases, diabetes, and kidney diseases.
  The plot effectively highlights how age is a significant factor in disease prevalence, with older age groups experiencing higher rates of various diseases.
Visualizations:
1.	Histogram:
o	Shows the distribution of disease values per 100,000, highlighting the frequency and spread.
  
2.	Stacked Bar Chart:
o	Represents disease distribution by state using custom colors for each disease category.
 
3.	Heatmap:
o	Visualizes average disease prevalence across states and age groups.
 
4.	Scatterplot:
o	Displays the relationship between age and disease incidence, with diseases colored according to the custom palette.
 

