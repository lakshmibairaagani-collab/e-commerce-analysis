# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
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
# ----------------------------------
# CORE FEATURE 1: Customer Purchase Analysis
# ----------------------------------

"""
Core Feature 1: Customer Purchase Analysis

This feature calculates total spending
for each customer and identifies the
top customers based on purchase amount.
"""

print("\nTop 10 Customers By Spending")

try:
    if df.empty:
        print("Error: Dataset is empty.")

    elif "CustomerID" not in df.columns:
        print("Error: CustomerID column missing.")

    elif "TotalAmount" not in df.columns:
        print("Error: TotalAmount column missing.")

    else:
        customer_sales = (
            df.groupby("CustomerID")["TotalAmount"]
            .sum()
            .sort_values(ascending=False)
        )

        print(customer_sales.head(10))

except Exception as e:
    print(f"Customer Purchase Analysis Error: {e}")


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

try:
    if df.empty:
        print("Error: Dataset is empty.")

    elif "InvoiceYear" not in df.columns:
        print("Error: InvoiceYear column missing.")

    elif "TotalAmount" not in df.columns:
        print("Error: TotalAmount column missing.")

    else:
        yearly_sales = (
            df.groupby("InvoiceYear")["TotalAmount"]
            .sum()
            .sort_index()
        )

        print(yearly_sales)

except Exception as e:
    print(f"Sales Trend Analysis Error: {e}")


# ----------------------------------
# CORE FEATURE 3: Product Performance Analysis
# ----------------------------------

"""
Core Feature 3: Product Performance Analysis

This feature identifies the top-selling products
based on total quantity sold.
"""

print("\nProduct Performance Analysis")

try:
    if df.empty:
        print("Error: Dataset is empty.")

    elif "Description" not in df.columns:
        print("Error: Description column missing.")

    elif "Quantity" not in df.columns:
        print("Error: Quantity column missing.")

    else:
        top_products = (
            df.groupby("Description")["Quantity"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
        )
    

        print(top_products)

except Exception as e:
    print(f"Product Performance Analysis Error: {e}")
    # ----------------------------------
# ADVANCED FEATURE 1:
# SALES VISUALIZATION DASHBOARD
# ----------------------------------

print("\nGenerating Sales Trend Chart...")

try:

    yearly_sales = (
        df.groupby("InvoiceYear")["TotalAmount"]
        .sum()
        .sort_index()
    )

    plt.figure(figsize=(8, 5))

    plt.plot(
        yearly_sales.index,
        yearly_sales.values,
        marker="o"
    )

    plt.title("Sales Trend by Year")
    plt.xlabel("Year")
    plt.ylabel("Total Sales")

    plt.grid(True)

    plt.savefig(
        "docs/images/sales_trend_dashboard.png"
    )

    plt.show()

    print("Sales dashboard created successfully!")

except Exception as e:
    print(f"Dashboard Error: {e}")