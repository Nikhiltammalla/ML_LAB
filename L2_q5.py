import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
file_path = "C:/Users/Nikhil/Downloads/Lab Session Data.xlsx"
df = pd.read_excel(file_path, sheet_name='thyroid0387_UCI')

# Display the first few rows of the dataframe
print(df.head())

# Identify the datatype for each attribute
print(df.info())

# Display the column names
print("Column names:", df.columns)

# Determine categorical and numeric columns programmatically
categorical_columns = df.select_dtypes(include=['object']).columns.tolist()
numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()

print("Categorical columns:", categorical_columns)
print("Numeric columns:", numeric_columns)

# Label Encoding for ordinal variables (none identified in this case)
label_encoders = {}
ordinal_columns = []  # Add any ordinal columns if identified
for col in ordinal_columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# One-Hot Encoding for nominal variables
df = pd.get_dummies(df, columns=categorical_columns, drop_first=True)

# Study the data range for numeric variables
print(df[numeric_columns].describe())

# Identify missing values in each attribute
missing_values = df.isnull().sum()
print("Missing values in each attribute:\n", missing_values)

# Detect outliers in the data using boxplots
for col in numeric_columns:
    plt.figure(figsize=(10, 5))
    sns.boxplot(x=df[col])
    plt.title(f'Boxplot for {col}')
    plt.show()

# Calculate the mean and variance (or standard deviation) for numeric variables
mean_values = df[numeric_columns].mean()
std_values = df[numeric_columns].std()
print("Mean values of numeric variables:\n", mean_values)
print("Standard deviation of numeric variables:\n", std_values)
