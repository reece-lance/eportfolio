# My Role and Contributions

---

- **Communication and Coordination:** Initiated and maintained team discussions through **WhatsApp** and forum threads, ensuring clear and consistent updates. This helped align all members on deadlines, expectations, and progress, preventing miscommunication and delays.
- **Project Planning and Task Assignment:** Organised the **workflow** by structuring a clear plan and delegating tasks based on individual strengths and availability. This approach ensured efficiency and balanced workload distribution.
- **Business Question Development:** Proposed the **core analytical question** that guided our data analysis, ensuring it was relevant to Airbnb’s business strategy and provided actionable insights.
- **Exploratory Data Analysis (EDA):** Worked alongside **Raluca** to conduct **EDA**, producing Python scripts to explore key patterns in the dataset, clean the data, and generate **visualisations** to support our findings.
- **Report Writing:** Contributed to the **writing and structuring** of the final analytical report, ensuring clarity, strong justifications, and effective presentation of data insights.
- **Final Submission:** Took responsibility for compiling and submitting the completed project, ensuring all components were properly formatted, complete, and aligned with the assignment requirements.
 
---

# Specific Examples of My Work

## 1. Demand and Availability Mapping

One of my key contributions was creating an **interactive clustered map** to visually represent the demand and availability of Airbnb listings across New York City neighborhoods. The map categorises areas into three types:

- **Green Markers:** High-demand, low-availability neighborhoods (ideal for new listings).
- **Orange Markers:** Borderline neighborhoods with moderate demand or availability.
- **Red Markers:** Areas to avoid due to low demand and high availability.

```python
from folium.plugins import MarkerCluster
import geopandas as gpd

# Load GeoJSON data for neighborhoods if centroids are needed
geo_data = gpd.read_file(geojson_path)
geo_data['centroid'] = geo_data['geometry'].centroid

# Create a clustered map
clustered_map = folium.Map(location=[40.7128, -74.0060], zoom_start=11)
marker_cluster = MarkerCluster().add_to(clustered_map)

# Add markers for high-demand neighborhoods (Green)
for _, row in high_demand_low_availability.iterrows():
    centroid = geo_data[geo_data['BoroName'] == row['neighbourhood']]['centroid']
    latitude = centroid.y.values[0] if not centroid.empty else data[data['neighbourhood'] == row['neighbourhood']]['latitude'].mean()
    longitude = centroid.x.values[0] if not centroid.empty else data[data['neighbourhood'] == row['neighbourhood']]['longitude'].mean()
    
    if pd.notnull(latitude) and pd.notnull(longitude):
        folium.Marker(
            location=[latitude, longitude],
            popup=create_popup(row, "Ideal: High Demand, Low Availability"),
            icon=folium.Icon(color='green', icon='star', prefix='fa')
        ).add_to(marker_cluster)

# Save the clustered map
clustered_map.save("../visualisations/clustered_map.html")
print("Clustered map saved as '../visualisations/clustered_map.html'.")
```
<iframe src="https://reece-lance.github.io/eportfolio/Machine_Learning/Team_Exercises/Examples/clustered_map.html" width="100%" height="600" style="border:0;" allowfullscreen></iframe>

---

## 2. Clustering Analysis with K-Means

I applied K-Means clustering to segment neighborhoods based on price, demand, and availability, allowing us to identify patterns and potential opportunities.

```python
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Select features for clustering
features = availability_price_analysis[['avg_price', 'avg_reviews', 'avg_availability']]

# Handle missing values (if any)
features = features.dropna()

# Scale the features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Apply k-means clustering with the optimal number of clusters
optimal_k = 3  # Determined from the Elbow Method
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
features['cluster'] = kmeans.fit_predict(scaled_features)

availability_price_analysis['cluster'] = features['cluster']
```

### Elbow Method for Choosing k:

To determine the optimal number of clusters, I used the Elbow Method to analyse inertia values across different k values.

```python
import matplotlib.pyplot as plt

# Calculate inertia for different k values
inertia = []
k_values = range(1, 10)
for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_features)
    inertia.append(kmeans.inertia_)

# Plot the Elbow Method
plt.figure(figsize=(8, 5))
plt.plot(k_values, inertia, marker='o')
plt.title('Elbow Method for Optimal k')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.show()
```

![image](https://github.com/user-attachments/assets/3d7a07fa-4b39-4645-b573-d6cd71fb139f)

---

## 3. Statistical Analysis: Pricing Differences Across Neighborhoods

To determine if Airbnb prices differ significantly across neighborhoods, I performed an ANOVA test.

```python
from scipy.stats import f_oneway

# Group data by neighbourhoods and extract price values
neighbourhood_groups = [filtered_data[filtered_data['neighbourhood'] == n]['avg_price'].dropna()
                        for n in filtered_data['neighbourhood'].unique()]

# Perform ANOVA test
f_statistic, p_value = f_oneway(*neighbourhood_groups)

print(f"ANOVA F-statistic: {f_statistic}, p-value: {p_value}")
```

A low p-value (typically < 0.05) would indicate significant pricing differences between neighborhoods.
A high p-value would suggest that pricing does not significantly vary by location.

### Conclusion

This project showcased my ability to apply data science techniques, such as exploratory data analysis, clustering, and data visualisation, to address real-world business challenges. By working collaboratively with my team, I contributed to uncovering actionable insights for Airbnb, such as identifying high-demand neighborhoods and areas to avoid. The final interactive maps, statistical analyses, and concise reporting provided a clear pathway for Airbnb to optimise its business strategy. This experience strengthened my technical expertise and teamwork skills, demonstrating my ability to deliver data-driven solutions effectively.
