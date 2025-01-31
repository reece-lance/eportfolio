# Jaccard Coefficient Calculations

## Task Overview
The Jaccard coefficient is a measure of similarity between two sets. It is calculated as the size of the intersection divided by the size of the union of the sets. In this task, we calculate the Jaccard coefficient for three individuals (Jack, Mary, and Jim) based on their pathological test results. The binary features include Fever, Cough, and four test results (Test-1 to Test-4).

## Code Implementation
```python
import numpy as np
import pandas as pd
from sklearn.metrics import jaccard_score

# Define the dataset as a DataFrame
data = pd.DataFrame({
    'Name': ['Jack', 'Mary', 'Jim'],
    'Gender': ['M', 'F', 'M'],
    'Fever': [1, 1, 1],  # Convert Y to 1
    'Cough': [0, 0, 1],  # Convert N to 0, P (Present) to 1
    'Test-1': [1, 1, 0],
    'Test-2': [0, np.nan, 0],  # A (Absent) to NaN
    'Test-3': [0, 1, 0],
    'Test-4': [np.nan, 0, np.nan]  # A (Absent) to NaN
})

# Fill NaN values with 0 for Jaccard similarity calculation
data_filled = data.fillna(0)

# Convert categorical features to numerical format (excluding Name and Gender)
features = data_filled.iloc[:, 2:].values

# Compute Jaccard similarity for each pair
pairs = [(0, 1), (0, 2), (1, 2)]  # Index pairs for (Jack, Mary), (Jack, Jim), (Jim, Mary)
results = {}
for (i, j) in pairs:
    similarity = jaccard_score(features[i], features[j])
    results[f"{data.iloc[i]['Name']} & {data.iloc[j]['Name']}"] = similarity

# Convert results to DataFrame and display
jaccard_df = pd.DataFrame(results.items(), columns=['Pair', 'Jaccard Coefficient'])
import ace_tools as tools
tools.display_dataframe_to_user(name="Jaccard Coefficients", dataframe=jaccard_df)
```

## Jaccard Coefficients

| Pair       | Jaccard Coefficient |
|------------|---------------------|
| Jack & Mary | 0.6667 |
| Jack & Jim  | 0.3333 |
| Mary & Jim  | 0.2500 |


## Reflection
### Knowledge of Machine Learning Algorithms
This task reinforced my understanding of similarity measures, specifically the Jaccard coefficient, which is commonly used in clustering and classification tasks when working with binary attributes. The ability to quantify similarity between individuals based on categorical data is crucial in medical diagnosis and recommendation systems.

### Individual Contributions
As this was an individual task, my focus was on implementing the Jaccard coefficient correctly, handling missing values appropriately, and ensuring accurate computation. I also structured the code in a way that allows easy extension to other similarity metrics if needed.

### Experience as a Team Member
Although this was an independent task, the skills developed—such as working with categorical data, data preprocessing, and implementing similarity measures—are applicable in collaborative projects. In a team setting, ensuring a clean and structured data preprocessing approach is critical for reproducibility and scalability.

### Impact on Professional/Personal Development
This task provided practical experience in working with categorical medical test data, an area relevant to real-world machine learning applications in healthcare and diagnostics. Additionally, improving my ability to handle missing values effectively and automate similarity calculations strengthens my data science expertise, which is valuable in professional settings.
