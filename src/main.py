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

print("\nWELCOME!")
print("This dashboard provides:")
print("1. Customer Purchase Analysis")
print("2. Sales Trend Analysis")
print("3. Product Performance Analysis")
print("4. Customer Segmentation")
print("5. Sales Visualization Dashboard")

print("\nPlease wait while data is processed...")

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
        print("No data found.")
        print("Please place cleaned_data.csv inside:")
        print("data/processed/")
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

        print("\nInsight:")
        print("These are the highest spending customers in the dataset.")
        print("They can be targeted for loyalty programs and promotions.")

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

        print("\nNote:")
        print("Sales values shown below are standardized (scaled) values.")
        print("Positive values indicate above-average sales.")
        print("Negative values indicate below-average sales.")

        print(yearly_sales)

        print("\nInsight:")
        print("This section shows how sales changed over the years.")
        print("Positive values indicate stronger sales performance.")

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

        print("\nInsight:")
        print("These are the best-selling products based on quantity sold.")
        print("They represent the most popular items among customers.")

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
    print("Dashboard saved at:")
    print("docs/images/sales_trend_dashboard.png")

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

    print("\nCustomer Categories:")
    print("Premium : Spending > 100")
    print("Regular : Spending between 50 and 100")
    print("Basic   : Spending <= 50")

except Exception as e:
    print(f"Customer Segmentation Error: {e}")

# ----------------------------------
# PROJECT SUMMARY
# ----------------------------------

print("\n" + "=" * 50)
print("PROJECT SUMMARY")
print("=" * 50)

print(f"Dataset Records: {len(df):,}")
print(f"Total Customers: {df['CustomerID'].nunique():,}")
print(f"Total Products: {df['Description'].nunique():,}")

print("\nGenerated Outputs:")
print("- Preprocessed Dataset")
print("- Sales Trend Dashboard")
print("- Customer Segmentation")
print("- Product Performance Analysis")

# ----------------------------------
# COMPLETION MESSAGE
# ----------------------------------

print("\n" + "=" * 50)
print("ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 50)

print("\nThank you for using the E-Commerce Analytics Dashboard.")