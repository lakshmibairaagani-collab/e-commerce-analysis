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

    print(f"Dataset Size: {len(df):,} rows")

    if len(df) > 1000000:
        print("Warning: Large dataset detected.")

    if df.empty:
        print("No data available for analysis.")
        exit()

    # Memory Optimization
    df["Quantity"] = pd.to_numeric(
        df["Quantity"],
        downcast="integer"
    )

    df["UnitPrice"] = pd.to_numeric(
        df["UnitPrice"],
        downcast="float"
    )

    print("Dataset loaded successfully!")

except Exception as e:
    print(f"Failed to load dataset: {e}")
    exit()

print("\nProcessing data...")

# ----------------------------------
# CREATE DERIVED FEATURES
# ----------------------------------

df["TotalAmount"] = df["Quantity"] * df["UnitPrice"]

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df["InvoiceYear"] = df["InvoiceDate"].dt.year

print("✓ New Features Created")

# ----------------------------------
# ENCODE CATEGORICAL VARIABLES
# ----------------------------------

df = pd.get_dummies(df, columns=["Country"])

print("✓ Encoding Completed")

# ----------------------------------
# SCALE NUMERICAL FEATURES
# ----------------------------------

scaler = StandardScaler()

df[["Quantity", "UnitPrice", "TotalAmount"]] = scaler.fit_transform(
    df[["Quantity", "UnitPrice", "TotalAmount"]]
)

print("✓ Scaling Completed")

# ----------------------------------
# TRAIN / TEST SPLIT
# ----------------------------------

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

# ----------------------------------
# SAVE PREPROCESSED DATASET
# ----------------------------------

os.makedirs("data/processed", exist_ok=True)

df.to_csv(
    "data/processed/preprocessed_data.csv",
    index=False
)

print("✓ Preprocessed dataset saved successfully!")

# ----------------------------------
# PERFORMANCE OPTIMIZATION
# ----------------------------------

print("\nOptimizing calculations...")

customer_sales = (
    df.groupby("CustomerID")["TotalAmount"]
    .sum()
)

yearly_sales = (
    df.groupby("InvoiceYear")["TotalAmount"]
    .sum()
    .sort_index()
)

product_sales = (
    df.groupby("Description")["Quantity"]
    .sum()
)

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

        print(
            customer_sales
            .sort_values(ascending=False)
            .head(10)
        )

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

        print(
            product_sales
            .sort_values(ascending=False)
            .head(10)
        )

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

    premium = customer_sales[
        customer_sales > 100
    ]

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