# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import os

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# ----------------------------------
# E-COMMERCE ANALYTICS DASHBOARD
# ----------------------------------

print("=" * 50)
print("E-COMMERCE CUSTOMER ANALYTICS DASHBOARD")
print("=" * 50)

print("\nLoading dataset...")

# ----------------------------------
# LOAD DATASET
# ----------------------------------

try:
    df = pd.read_csv("data/processed/cleaned_data.csv")

    if df.empty:
        print("No data available for analysis.")
        exit()

    print("Dataset loaded successfully!")

except Exception as e:
    print(f"Failed to load dataset: {e}")
    exit()

print("\nProcessing data...")

# -------------------------
# Create Derived Features
# -------------------------

# Feature 1: Calculate total transaction amount
df["TotalAmount"] = df["Quantity"] * df["UnitPrice"]

# Feature 2: Extract year from invoice date
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df["InvoiceYear"] = df["InvoiceDate"].dt.year

print("✓ New Features Created")

# -------------------------
# Encode Categorical Variables
# -------------------------

df = pd.get_dummies(df, columns=["Country"])

print("✓ Encoding Completed")

# -------------------------
# Scale Numerical Features
# -------------------------

scaler = StandardScaler()

df[["Quantity", "UnitPrice", "TotalAmount"]] = scaler.fit_transform(
    df[["Quantity", "UnitPrice", "TotalAmount"]]
)

print("✓ Scaling Completed")

# -------------------------
# Train/Test Split
# -------------------------

X = df.drop("CustomerID", axis=1)
y = df["CustomerID"]

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

os.makedirs("data/processed", exist_ok=True)

df.to_csv(
    "data/processed/preprocessed_data.csv",
    index=False
)

print("✓ Preprocessed dataset saved successfully!")

# ----------------------------------
# CORE FEATURE 1
# CUSTOMER PURCHASE ANALYSIS
# ----------------------------------

print("\n" + "=" * 50)
print("TOP 10 CUSTOMERS BY SPENDING")
print("=" * 50)

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
# CORE FEATURE 2
# SALES TREND ANALYSIS
# ----------------------------------

print("\n" + "=" * 50)
print("SALES TREND ANALYSIS")
print("=" * 50)

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
# CORE FEATURE 3
# PRODUCT PERFORMANCE ANALYSIS
# ----------------------------------

print("\n" + "=" * 50)
print("PRODUCT PERFORMANCE ANALYSIS")
print("=" * 50)

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
# ADVANCED FEATURE 1
# SALES VISUALIZATION DASHBOARD
# ----------------------------------

print("\n" + "=" * 50)
print("SALES VISUALIZATION DASHBOARD")
print("=" * 50)

print("Generating Sales Trend Chart...")

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

# ----------------------------------
# ADVANCED FEATURE 2
# CUSTOMER SEGMENTATION
# ----------------------------------

print("\n" + "=" * 50)
print("CUSTOMER SEGMENTATION")
print("=" * 50)

try:

    customer_sales = (
        df.groupby("CustomerID")["TotalAmount"]
        .sum()
    )

    premium = customer_sales[customer_sales > 100]

    regular = customer_sales[
        (customer_sales > 50)
        & (customer_sales <= 100)
    ]

    basic = customer_sales[
        customer_sales <= 50
    ]

    print("Premium Customers:", len(premium))
    print("Regular Customers:", len(regular))
    print("Basic Customers:", len(basic))

except Exception as e:
    print(f"Customer Segmentation Error: {e}")

# ----------------------------------
# COMPLETION MESSAGE
# ----------------------------------

print("\n" + "=" * 50)
print("ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 50)