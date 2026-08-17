import pandas as pd

# Load the dataset
df = pd.read_csv("C:/Users/CC/Downloads/student_data.csv")
print(df)

print("=" * 60)
print("1. DATASET PREVIEW")
print("=" * 60)

# PURPOSE: df.head() displays the first 5 rows of the DataFrame.
print(df.head(), "\n")

print("=" * 60)
print("2. DATASET SHAPE")
print("=" * 60)

# PURPOSE: df.shape returns the number of rows and columns in the DataFrame.
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}\n")
print("=" * 60)
print("3. COLUMN NAMES")
print("=" * 60)

# PURPOSE: df.columns returns all column names in the DataFrame.
print(df.columns.tolist(), "\n")

print("=" * 60)
print("4. DATASET INFORMATION")
print("=" * 60)

# PURPOSE: df.info() prints a concise summary of the DataFrame, including memory usage, index dtype, column dtypes, and non-null values.
df.info()
print("\n")

print("=" * 60)
print("5. MISSING VALUES CHECK")
print("=" * 60)

# PURPOSE: df.isnull() detects missing values (NaN) returning a boolean mask, and .sum() aggregates those True values.
missing_data = df.isnull().sum()

print(
    missing_data[missing_data > 0]
    if missing_data.sum() > 0
    else "No missing values found."
)

print("\n")
