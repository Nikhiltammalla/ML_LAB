import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Load the data from the Excel file
file_path = "C:/Users/Nikhil/Downloads/Lab Session Data.xlsx"
thyroid_data = pd.read_excel(file_path, sheet_name='thyroid0387_UCI')

# Select numerical columns
numerical_columns = thyroid_data.select_dtypes(include=['int64']).columns

# Display statistics for numerical columns
print(thyroid_data[numerical_columns].describe())

# High standard deviation for 'age'
scaler = StandardScaler()
thyroid_data['age'] = scaler.fit_transform(thyroid_data[['age']])

# Print the Z-score normalized 'age' column
print("Z-score Normalized 'age' Column:")
print(thyroid_data['age'])