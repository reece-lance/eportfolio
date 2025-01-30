# Task: Regression and Correlation Analysis Using Car Data

## Task Overview
This task focuses on understanding the relationships between **engine volume, car weight, and CO2 emissions** using **correlation, covariance, linear regression, multiple linear regression, and polynomial regression**. These techniques help analyze how different features influence CO2 emissions and assess the suitability of different regression models.

---

## Code: Regression and Correlation Analysis

### **1. Covariance & Pearson Correlation Analysis**
```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("cars.csv")

# Compute covariance matrix
cov_matrix = df[['Volume', 'Weight', 'CO2']].cov()

# Compute Pearson correlation matrix
corr_matrix = df[['Volume', 'Weight', 'CO2']].corr()

# Display matrices
print("Covariance Matrix:\n", cov_matrix)
print("\nPearson Correlation Matrix:\n", corr_matrix)

# Heatmap of correlation matrix
plt.figure(figsize=(6,4))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Pearson Correlation Heatmap")
plt.show()
```

![image](https://github.com/user-attachments/assets/cd4fd351-8d87-4bea-9cbf-3eb5c6f9bbc4)

### **2. Linear Regression**
```python
from sklearn.linear_model import LinearRegression

# Define independent (X) and dependent (y) variables
X = df[['Volume']].values  # Engine Volume as predictor
y = df['CO2'].values  # CO2 emissions as target variable

# Initialize and fit the linear regression model
linear_model = LinearRegression()
linear_model.fit(X, y)

# Get model parameters
slope = linear_model.coef_[0]
intercept = linear_model.intercept_

print(f"Linear Regression Equation: CO2 = {slope:.4f} * Volume + {intercept:.2f}")

# Plot regression line
plt.scatter(df['Volume'], df['CO2'], color='blue', label="Actual Data")
plt.plot(df['Volume'], linear_model.predict(X), color='red', label="Regression Line")
plt.xlabel("Engine Volume")
plt.ylabel("CO2 Emissions")
plt.title("Linear Regression: CO2 vs Engine Volume")
plt.legend()
plt.show()
```

![image](https://github.com/user-attachments/assets/585159c1-0657-437b-ada0-621fe5e02d11)

### **3. Multiple Linear Regression**
```python
# Define independent (X) and dependent (y) variables for multiple linear regression
X_multi = df[['Volume', 'Weight']].values  # Multiple predictors
y_multi = df['CO2'].values  # CO2 emissions as target variable

# Initialize and fit the multiple linear regression model
multi_linear_model = LinearRegression()
multi_linear_model.fit(X_multi, y_multi)

# Get model parameters
multi_slope = multi_linear_model.coef_
multi_intercept = multi_linear_model.intercept_

print(f"Multiple Linear Regression Equation: CO2 = {multi_slope[0]:.4f} * Volume + {multi_slope[1]:.4f} * Weight + {multi_intercept:.2f}")
```

**Output:**
Multiple Linear Regression Equation: CO2 = 0.0078 * Volume + 0.0076 * Weight + 79.69

### **4. Polynomial Regression**
```python
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

# Define independent (X) and dependent (y) variables
X_poly = df[['Volume']].values  # Using only Volume for polynomial regression
y_poly = df['CO2'].values

# Create a polynomial regression model (degree=2)
poly_model = make_pipeline(PolynomialFeatures(degree=2), LinearRegression())
poly_model.fit(X_poly, y_poly)

# Get model coefficients
poly_regressor = poly_model.named_steps['linearregression']
poly_coefficients = poly_regressor.coef_
poly_intercept = poly_regressor.intercept_

print(f"Polynomial Regression Equation: CO2 = {poly_coefficients[1]:.6f} * Volume + {poly_coefficients[2]:.6f} * Volume^2 + {poly_intercept:.2f}")

# Plot polynomial regression curve
X_range = np.linspace(df['Volume'].min(), df['Volume'].max(), 100).reshape(-1, 1)
plt.scatter(df['Volume'], df['CO2'], color='blue', label="Actual Data")
plt.plot(X_range, poly_model.predict(X_range), color='green', label="Polynomial Fit")
plt.xlabel("Engine Volume")
plt.ylabel("CO2 Emissions")
plt.title("Polynomial Regression: CO2 vs Engine Volume")
plt.legend()
plt.show()
```

![image](https://github.com/user-attachments/assets/0eb1dc13-412c-464d-ac1e-334564a21a94)

---

## **Reflection**

### **Knowledge of Machine Learning Algorithms**
This task helped reinforce my understanding of **regression analysis** and the differences between various models:
- **Linear Regression** showed a **direct relationship** between **engine volume and CO2 emissions**.
- **Multiple Linear Regression** improved predictive accuracy by incorporating both **engine volume and weight**.
- **Polynomial Regression** demonstrated that relationships between variables **may not always be linear**, highlighting the importance of model selection.

### **Individual Contributions**
As an individual assignment, this task allowed me to independently apply **various regression techniques** and evaluate their effectiveness in real-world datasets. Understanding the theoretical foundations of **covariance and correlation** was essential in determining which features significantly impact CO2 emissions.

### **Experience as a Development Team Member**
Although this was an individual task, the skills developed—such as **data preprocessing, regression modeling, and visualization**—are highly applicable in **team projects**. These skills contribute to **collaborative data analysis**, ensuring that findings are well-communicated and interpreted effectively in a group setting.

### **Impact on Professional & Personal Development**
This exercise strengthened my ability to apply **data-driven decision-making** to real-world scenarios, particularly in **environmental impact analysis**. Understanding how variables interact in regression models is a fundamental skill in **data science, business intelligence, and predictive modeling**. The visualization techniques also helped refine my ability to **present analytical findings clearly**, a valuable skill in both academic and professional settings.
