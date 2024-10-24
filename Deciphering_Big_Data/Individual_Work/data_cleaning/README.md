# Data Cleaning Task

### Task Description

This task involved cleaning and processing a 9,008-row, 159-column Unicef dataset to prepare it for analysis and store it in a SQLite database. Key steps included header replacement, resolving column mismatches, removing duplicates, handling missing values, normalising data, and ensuring SQLite compatibility.

### Learning Objectives

- Understand and apply data cleaning techniques.
- Evaluate outcomes for data design and automation.
- Compile and document Python scripts.
- Convert datasets into various formats.

### Detailed Objectives

- **Load the dataset** and ensure it is correctly read into memory.
- **Replace headers** from a provided header file, resolving any mismatches.
- **Handle column mismatches** by aligning headers with the dataset.
- **Remove duplicates** to maintain data consistency.
- **Handle missing values** by filling numeric columns with mean values.
- **Normalise numeric data** for consistent scaling.
- **Sanitise column names** for SQLite compatibility.
- **Save the cleaned dataset** into a SQLite database for querying and analysis.

## Steps Completed

### 1. **Data Loading**
   - The dataset was successfully loaded with 9,008 rows and 159 columns.
   - A separate header file containing 210 headers was provided, which resulted in a mismatch with the dataset. The headers were truncated to match the 159 columns in the dataset.

### 2. **Replacing Headers**
   - The headers were replaced successfully after truncating them to align with the number of columns in the dataset.

### 3. **Handling Column Mismatches**
   - A mismatch between the number of headers and data columns was handled by truncating the header file to ensure alignment.
   - No missing headers were identified that would impact the data analysis.

### 4. **Removing Duplicates**
   - Duplicates were removed from the dataset, retaining a total of 9,008 unique records.

### 5. **Handling Missing Values**
   - Numeric columns with missing values were filled using the mean of each respective column.

### 6. **Normalising Numeric Data**
   - The numeric columns were normalised, ensuring consistent scaling across the dataset for future analysis.

### 7. **Sanitising Column Names for SQLite**
   - The column names were sanitised by removing special characters and ensuring each column name is unique, making the dataset compatible with SQLite.

### 8. **Saving to SQLite**
   - The cleaned dataset was saved to an SQLite database (`cleaned_data.db`) in the table `cleaned_data`. The data is now accessible for querying and analysis using SQL commands.

## Results

- The final cleaned dataset contains 9,008 rows and 159 columns.
- The data has been cleaned, normalised, and stored in an [SQLite database (`cleaned_data.db`)](./data/cleaned_data.db), where it can be easily accessed and queried.

## Instructions for Running the [Code](./data-cleaning.py)

### Prerequisites

- Ensure Python 3.x is installed along with the required libraries:
  ```bash
  pip install pandas numpy sqlite3

---

## References

