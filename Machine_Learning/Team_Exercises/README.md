# My Role and Contributions

---

- **Communication and Coordination:** Initiated communication through WhatsApp and forum threads to ensure clear, consistent updates and collaboration. This approach helped prevent miscommunications and ensured all team members were aligned on the project objectives and deadlines.
- **Task Assignment and Planning:** Created a detailed project plan and assigned tasks based on team members' strengths and availability. This strategy optimised workflow and helped meet deadlines efficiently.
- **Data Management Pipeline Development:** Led the design and implementation of a data management pipeline using Python. This included:
  - **Data Retrieval:** Developed Python scripts to access TfL's API, retrieve data in various formats (JSON, ZIP), and save it locally for further processing.
  - **Data Cleaning:** Implemented data cleaning techniques, such as handling missing values and removing duplicates, using Python libraries (e.g., `pandas`).
  - **Data Preparation for Database Loading:** Structured the cleaned data to be compatible with the chosen DBMS format, including normalising data to reduce redundancy.
 
---

# Specific Examples of My Work

## 1. Data Retrieval and Processing Script

To automate data retrieval from TfL's API, I developed a Python script that fetches data from multiple endpoints, handles different file types (e.g., JSON, ZIP), and stores them in the appropriate directory for further processing:

```python
import requests
import zipfile
import io
import os

def fetch_and_process_data(url, files_list):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            content_type = response.headers.get('Content-Type', '')
            file_name = url.split('/')[-1]
            base_name, file_extension = os.path.splitext(file_name)
            directory_name = base_name.replace('.', '_')
            raw_data_path = os.path.join("..", "data", "raw", directory_name)
            os.makedirs(raw_data_path, exist_ok=True)

            if 'zip' in content_type or file_extension == '.zip':
                with zipfile.ZipFile(io.BytesIO(response.content)) as zip_file:
                    for file_info in zip_file.infolist():
                        zip_file.extract(file_info, raw_data_path)
                        extracted_file_path = os.path.join(raw_data_path, file_info.filename)
                        files_list.append(extracted_file_path)
                print(f"Data downloaded and extracted successfully to {raw_data_path}.")
            else:
                file_path = os.path.join(raw_data_path, file_name)
                with open(file_path, 'wb') as file:
                    file.write(response.content)
                files_list.append(file_path)
                print(f"Data downloaded successfully and saved as {file_path}.")
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
            
        return files_list

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching data: {e}")

# List of endpoints and processing loop
URL_NAME = "https://api.tfl.gov.uk"
endpoints = ["/stationdata/tfl-stationdata-detailed.zip", "/Line/Route", "/Vehicle/{ids}/Arrivals"]
files_list = []
for endpoint in endpoints:
    files_list = fetch_and_process_data(URL_NAME + endpoint, files_list)
```

<iframe src="./Team_Exercises/Examples/map.html" width="100%" height="600" style="border:0;" allowfullscreen></iframe>

---

## 2. Data Cleaning and Preparation
After retrieving the data, I implemented data cleaning procedures to handle missing values and remove duplicates:

```python
Copy code
import pandas as pd

df = pd.read_json('raw_data.json')
df.drop_duplicates(inplace=True)
df.fillna(method='ffill', inplace=True)  # Fill missing values using forward fill method
df.to_csv('cleaned_data.csv', index=False)
print("Data cleaning completed and saved as cleaned_data.csv.")
```
### Conclusion

This project was a valuable learning experience in database design, data management, and teamwork. It equipped me with essential skills for future professional roles in data science and reinforced the importance of clear communication, detailed analysis, and a focus on core requirements.
