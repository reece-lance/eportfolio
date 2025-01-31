# K-Means Clustering Analysis

## Task Overview
K-Means clustering is an unsupervised learning algorithm used to group data points into clusters based on feature similarity. The objective of this task was to apply K-Means clustering to three datasets: **Iris, Wine, and WeatherAUS**. The tasks involved:
- Preprocessing the data by handling missing values and scaling features.
- Determining the optimal number of clusters (*K*) using the **Elbow Method**.
- Applying **K-Means clustering** with K=3.
- Visualising the results using **PCA-reduced scatter plots**.
- Evaluating clustering quality using the **Silhouette Score**.

## Code Implementation

### **Iris Dataset**
```python
# Load and preprocess data
iris_df = pd.read_csv('iris.csv')
iris_data = iris_df.drop(columns=['species'])  # Remove categorical column
scaler = StandardScaler()
scaled_iris = scaler.fit_transform(iris_data)

# Apply K-Means with K=3
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
iris_clusters = kmeans.fit_predict(scaled_iris)

# PCA for visualisation
pca = PCA(n_components=2)
reduced_iris = pca.fit_transform(scaled_iris)

# Scatter plot of clusters
sns.scatterplot(x=reduced_iris[:, 0], y=reduced_iris[:, 1], hue=iris_clusters, 
                palette=["#1f77b4", "#ff7f0e", "#2ca02c"], alpha=0.8)
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("K-Means Clustering (K=3) - Iris Dataset")
plt.show()
```

![image](https://github.com/user-attachments/assets/70a09400-aa32-4b07-abb4-9607dbc82f2f)

![image](https://github.com/user-attachments/assets/ea0b23ed-0869-4a54-b619-60ba2ceb94a8)

### **Wine Dataset**
```python
# Load and preprocess data
wine_df = pd.read_csv('wine.csv')
wine_data = wine_df.drop(columns=['Wine'])  # Remove categorical column
scaler = StandardScaler()
scaled_wine = scaler.fit_transform(wine_data)

# Apply K-Means with K=3
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
wine_clusters = kmeans.fit_predict(scaled_wine)

# PCA for visualisation
pca = PCA(n_components=2)
reduced_wine = pca.fit_transform(scaled_wine)

# Scatter plot of clusters
sns.scatterplot(x=reduced_wine[:, 0], y=reduced_wine[:, 1], hue=wine_clusters, 
                palette=["#1f77b4", "#ff7f0e", "#2ca02c"], alpha=0.8)
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("K-Means Clustering (K=3) - Wine Dataset")
plt.show()
```

![image](https://github.com/user-attachments/assets/3b020d42-d750-40c8-8e1d-dfac6b08b355)

![image](https://github.com/user-attachments/assets/42f9a97b-a23f-4732-8f1a-9e282c2a6ba5)

### **WeatherAUS Dataset**
```python
# Load and preprocess data
weather_df = pd.read_csv('weatherAUS.csv')
weather_data = weather_df.drop(columns=['RainToday', 'RainTomorrow'], errors='ignore').dropna()
scaler = StandardScaler()
scaled_weather = scaler.fit_transform(weather_data)

# Apply K-Means with K=3
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
weather_clusters = kmeans.fit_predict(scaled_weather)

# PCA for visualisation
pca = PCA(n_components=2)
reduced_weather = pca.fit_transform(scaled_weather)

# Scatter plot of clusters
sns.scatterplot(x=reduced_weather[:, 0], y=reduced_weather[:, 1], hue=weather_clusters, 
                palette=["#1f77b4", "#ff7f0e", "#2ca02c"], alpha=0.8)
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("K-Means Clustering (K=3) - WeatherAUS Dataset")
plt.show()
```

![image](https://github.com/user-attachments/assets/3238eb4a-5fe9-42e5-9485-5acef6cfc017)

![image](https://github.com/user-attachments/assets/4f8a7a97-73de-406c-828b-409224fae4a7)

## Reflection
### **Knowledge of Machine Learning Algorithms**
This task deepened my understanding of **K-Means clustering**, particularly in the context of **high-dimensional data**. I reinforced my knowledge of **feature scaling** and its importance in clustering algorithms reliant on **Euclidean distance**.

### **Individual Contributions**
I independently conducted **data preprocessing**, cluster analysis, and visualisation for each dataset. Applying **PCA** for dimensionality reduction significantly improved cluster interpretability.

### **Experience as a Team Member**
Although this was an individual task, the insights gained here contribute to my ability to collaborate effectively in team projects. Understanding **cluster validity metrics** will support my participation in discussions about model evaluation in future tasks.

### **Impact on Professional Development**
Performing this analysis improved my **Python programming skills**, particularly in using **scikit-learn for clustering**, **Matplotlib for visualisation**, and **Pandas for data preprocessing**. These are valuable skills applicable to roles in **data science and analytics**.
