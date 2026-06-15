import pandas as pd

# Load dataset
df = pd.read_csv("data/data.csv", encoding="latin1")

print("Original Shape:", df.shape)

# -------------------------
# Handle Missing Values
# -------------------------

# Fill missing descriptions
df["Description"] = df["Description"].fillna("Unknown")

# Keep CustomerID missing values for now
# or fill with 0
df["CustomerID"] = df["CustomerID"].fillna(0)

# -------------------------
# Remove Duplicate Rows
# -------------------------

duplicates_before = df.duplicated().sum()
print("Duplicate Rows:", duplicates_before)

df = df.drop_duplicates()

print("Shape After Removing Duplicates:", df.shape)

# -------------------------
# Fix Data Types
# -------------------------

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

df["CustomerID"] = df["CustomerID"].astype(int)

# -------------------------
# Save Cleaned Dataset
# -------------------------

df.to_csv(
    "data/processed/cleaned_data.csv",
    index=False
)

print("Cleaned dataset saved successfully!")