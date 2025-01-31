# Linear Regression with Scikit-Learn

## Task Overview

In this task, we explored the relationship between **Mean Population** (2001-2020) and **Mean GDP** (2001-2020) using correlation and regression analysis. The dataset used included:
- `Global_GDP.csv`: GDP data for various countries.
- `Global_Population.csv`: Population data for the same countries.

We performed two main tasks:
- **Task A: Correlation Analysis**: Investigated the correlation between mean population and mean per capita GDP.
- **Task B: Regression Analysis**: Built a linear regression model with mean population as the independent variable and mean GDP as the dependent variable.

---

## Code

### Data Preprocessing
```python
import pandas as pd

# Load datasets
gdp_file = "Global_GDP.csv"
population_file = "Global_Population.csv"
gdp_df = pd.read_csv(gdp_file)
population_df = pd.read_csv(population_file)

# Select relevant years (2001-2020)
years = [str(year) for year in range(2001, 2021)]

# Filter and calculate the mean values for GDP and Population
gdp_filtered = gdp_df[['Country Name', 'Country Code'] + years].dropna()
population_filtered = population_df[['Country Name', 'Country Code'] + years].dropna()

# Convert to numeric format
gdp_filtered[years] = gdp_filtered[years].apply(pd.to_numeric, errors='coerce')
population_filtered[years] = population_filtered[years].apply(pd.to_numeric, errors='coerce')

# Compute mean GDP and mean population
gdp_filtered['Mean GDP'] = gdp_filtered[years].mean(axis=1)
population_filtered['Mean Population'] = population_filtered[years].mean(axis=1)

# Merge datasets
merged_df = pd.merge(
    gdp_filtered[['Country Name', 'Country Code', 'Mean GDP']],
    population_filtered[['Country Name', 'Country Code', 'Mean Population']],
    on=['Country Name', 'Country Code']
)

# Drop missing values
merged_df.dropna(inplace=True)
```

### Correlation Analysis
```python
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

# Scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x=merged_df['Mean Population'], y=merged_df['Mean GDP'])
plt.xlabel("Mean Population (2001-2020)")
plt.ylabel("Mean GDP (2001-2020)")
plt.title("Correlation between Mean Population and Mean GDP")
plt.xscale("log")
plt.yscale("log")
plt.show()

# Pearson Correlation Coefficient
correlation_coefficient, p_value = pearsonr(merged_df['Mean Population'], merged_df['Mean GDP'])
print(f"Pearson Correlation Coefficient: {correlation_coefficient}")
print(f"P-value: {p_value}")
```

![image](https://github.com/user-attachments/assets/2119e554-3e03-4f7b-9da7-47c0c7ea7dff)

### Regression Analysis
```python
from sklearn.linear_model import LinearRegression
import numpy as np

# Define independent and dependent variables
X = merged_df[['Mean Population']].values.reshape(-1, 1)
y = merged_df['Mean GDP'].values

# Linear Regression model
regression_model = LinearRegression()
regression_model.fit(X, y)

# Predictions
y_pred = regression_model.predict(X)

# Improved Regression Plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x=merged_df['Mean Population'], y=merged_df['Mean GDP'], label="Actual Data", alpha=0.7, edgecolor=None)

# Sort data for plotting the regression line
sorted_indices = np.argsort(merged_df['Mean Population'])
plt.plot(merged_df['Mean Population'].values[sorted_indices], y_pred[sorted_indices], color='red', linewidth=2, label="Regression Line")

# Improve axis labels and title
plt.xlabel("Mean Population (2001-2020)", fontsize=12)
plt.ylabel("Mean GDP (2001-2020)", fontsize=12)
plt.title("Linear Regression: Mean Population Vs. Mean GDP", fontsize=14, fontweight='bold')

# Set log scale for better data distribution
plt.xscale("log")
plt.yscale("log")
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.legend()
plt.show()

# Model Coefficients
slope = regression_model.coef_[0]
intercept = regression_model.intercept_
print(f"Slope: {slope}, Intercept: {intercept}")
```



![image](https://github.com/user-attachments/assets/4b4be529-819f-49fa-85d5-dfeaf5b21611)

---

## Reflections

### Knowledge of Machine Learning Algorithms
This task reinforced my understanding of **correlation analysis** and **linear regression**. The correlation analysis revealed a **strong positive relationship** between population and GDP, quantified using Pearson's correlation coefficient. The regression model further demonstrated how we could use population data to estimate GDP values.

### Individual Contribution
I individually implemented the **data preprocessing, correlation analysis, and regression model**, ensuring the results were interpretable. By handling missing values effectively and structuring the analysis logically, I ensured that the insights were valid and relevant.

### Experience as a Development Team Member
Although this was an individual task, I consulted with my team to cross-check results and interpretations. This helped validate my findings and understand how others approached similar issues.

### Impact on Professional/Personal Development
This task improved my ability to **clean and preprocess real-world datasets**, handle **missing data**, and apply **machine learning techniques** effectively. Additionally, learning how to communicate findings through **visualisations** and numerical analysis will be valuable in a data science role.
