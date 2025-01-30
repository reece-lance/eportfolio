# Exploratory Data Analysis (EDA) on the Auto-mpg Dataset

## **Task Overview**
This task involved performing **Exploratory Data Analysis (EDA)** on the **Auto-mpg dataset** to explore and understand the data before applying machine learning techniques. The key objectives were:

1. Identifying and handling missing values.
2. Estimating **skewness** and **kurtosis** for numerical columns.
3. Generating a **correlation heatmap** to observe relationships between variables.
4. Creating **scatter plots** for different parameters.
5. Replacing categorical values with numerical values.

---

## **Code Implementation**

### **Step 1: Identifying Missing Values**
```python
import pandas as pd

# Load dataset
df = pd.read_csv("auto-mpg.csv")

# Check for missing values
df.replace("?", pd.NA, inplace=True)  # Replace '?' with NaN
df.isnull().sum()
```
**Findings:** Six missing values were found in the `horsepower` column.

### **Step 2: Handling Missing Values**
```python
# Convert horsepower to numeric and replace NaNs with median
df['horsepower'] = pd.to_numeric(df['horsepower'], errors='coerce')
df['horsepower'].fillna(df['horsepower'].median(), inplace=True)
```

### **Step 3: Estimating Skewness and Kurtosis**
```python
import numpy as np

# Compute skewness and kurtosis
skewness = df.skew()
kurtosis = df.kurt()
skewness, kurtosis
```
**Findings:** The `horsepower` and `origin` columns showed high skewness.

### **Step 4: Generating a Correlation Heatmap**
```python
import seaborn as sns
import matplotlib.pyplot as plt

# Compute correlation matrix with only numerical columns
plt.figure(figsize=(10,6))
sns.heatmap(df.select_dtypes(include=['number']).corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()
```

![image](https://github.com/user-attachments/assets/0824bb6e-4c89-43df-b219-39f9e37c4737)


**Findings:** `MPG` was strongly **negatively correlated** with `weight`, `horsepower`, and `displacement`.

### **Step 5: Scatter Plots for Key Relationships**
```python
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Scatter plot of MPG vs Weight
axes[0, 0].scatter(df['weight'], df['mpg'], alpha=0.5)
axes[0, 0].set_xlabel("Weight")
axes[0, 0].set_ylabel("MPG")
axes[0, 0].set_title("MPG vs Weight")

# Scatter plot of Horsepower vs MPG
axes[0, 1].scatter(df['horsepower'], df['mpg'], alpha=0.5, color='r')
axes[0, 1].set_xlabel("Horsepower")
axes[0, 1].set_ylabel("MPG")
axes[0, 1].set_title("MPG vs Horsepower")

plt.tight_layout()
plt.show()
```

![image](https://github.com/user-attachments/assets/1e2b5124-9021-48fc-918a-fed5da6afafd)

**Findings:** As expected, **MPG decreases as weight, horsepower, and engine displacement increase**.

### **Step 6: Replacing Categorical Values**
```python
# Convert 'origin' categorical values to numerical
origin_mapping = {1: 'America', 2: 'Europe', 3: 'Asia'}
df['origin'] = df['origin'].replace(origin_mapping)
df['origin'] = df['origin'].astype('category').cat.codes  # America=0, Europe=1, Asia=2
```

---

## **Reflection**

### **Knowledge of Machine Learning Algorithms**
This task reinforced my understanding of **EDA**, a critical step before applying machine learning algorithms. Understanding **data distributions, correlations, and missing values** is essential for model performance.

### **Individual Contributions**
I independently cleaned and processed the dataset, handled missing values using **median imputation**, and visualised relationships between variables. This strengthened my ability to **prepare data effectively** for machine learning models.

### **Experience as a Team Member**
Although this was an individual task, the insights gained from EDA are valuable for collaborative data projects. Effective **data preparation and visualisation** are key discussion points when working with a team to develop predictive models.

### **Impact on Professional Development**
This task enhanced my ability to work with real-world datasets using **Pandas, Seaborn, and Matplotlib**. Understanding **correlations and distributions** has improved my confidence in data-driven decision-making, an essential skill in data science and analytics.

---

### **Final Thoughts**
By conducting this EDA, I developed a stronger foundation in **data preprocessing**, which is a crucial step in any machine learning pipeline. This hands-on experience has refined my **technical and analytical skills**, preparing me for more complex data challenges in the future.
