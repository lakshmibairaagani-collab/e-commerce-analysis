# Import required libraries
import pandas as pd
import os

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Load the cleaned dataset
df = pd.read_csv("data/processed/cleaned_data.csv")

# -------------------------
# Create Derived Features
# -------------------------

# Feature 1: Calculate total transaction amount
df["TotalAmount"] = df["Quantity"] * df["UnitPrice"]

# Feature 2: Extract year from invoice date
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df["InvoiceYear"] = df["InvoiceDate"].dt.year

print("New Features Created")

# -------------------------
# Encode Categorical Variables
# -------------------------

# Convert Country column into numerical columns
df = pd.get_dummies(df, columns=["Country"])

print("Encoding Completed")

# -------------------------
# Scale Numerical Features
# -------------------------

# Standardize numerical features
scaler = StandardScaler()

df[["Quantity", "UnitPrice", "TotalAmount"]] = scaler.fit_transform(
    df[["Quantity", "UnitPrice", "TotalAmount"]]
)

print("Scaling Completed")

# -------------------------
# Train/Test Split
# -------------------------

# Separate features and target variable
X = df.drop("CustomerID", axis=1)
y = df["CustomerID"]

# Split dataset into 80% training and 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("Training Set Shape:", X_train.shape)
print("Testing Set Shape:", X_test.shape)

# -------------------------
# Save Preprocessed Dataset
# -------------------------

# Create processed folder if it doesn't exist
os.makedirs("data/processed", exist_ok=True)

# Save final preprocessed dataset
df.to_csv(
    "data/processed/preprocessed_data.csv",
    index=False
)

print("Preprocessed dataset saved successfully!")
"""
Core Feature 1: Customer Purchase Analysis

This feature calculates total spending
for each customer and identifies the
top customers based on purchase amount.
"""

print("\nTop 10 Customers By Spending")

if df.empty:
    print("Dataset is empty.")

elif "CustomerID" not in df.columns:
    print("CustomerID column missing.")

elif "TotalAmount" not in df.columns:
    print("TotalAmount column missing.")

else:
    customer_sales = (
        df.groupby("CustomerID")["TotalAmount"]
        .sum()
        .sort_values(ascending=False)
    )

    print(customer_sales.head(10))
    # ----------------------------------
# CORE FEATURE 2: Sales Trend Analysis
# ----------------------------------

"""
Core Feature 2: Sales Trend Analysis

This feature analyzes sales trends by year
using the TotalAmount feature created during
preprocessing.
"""

print("\nSales Trend Analysis")

if df.empty:
    print("Dataset is empty.")

elif "InvoiceYear" not in df.columns:
    print("InvoiceYear column missing.")

elif "TotalAmount" not in df.columns:
    print("TotalAmount column missing.")

else:
    yearly_sales = (
        df.groupby("InvoiceYear")["TotalAmount"]
        .sum()
        .sort_index()
    )

    print(yearly_sales)