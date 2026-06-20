import pandas as pd
import os

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Load cleaned dataset
df = pd.read_csv("data/processed/cleaned_data.csv")

# -------------------------
# Create Derived Features
# -------------------------

# Feature 1
df["TotalAmount"] = df["Quantity"] * df["UnitPrice"]

# Feature 2
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df["InvoiceYear"] = df["InvoiceDate"].dt.year

print("New Features Created")

# -------------------------
# Encode Categorical Variables
# -------------------------

df = pd.get_dummies(df, columns=["Country"])

print("Encoding Completed")

# -------------------------
# Scale Numerical Features
# -------------------------

scaler = StandardScaler()

df[["Quantity", "UnitPrice", "TotalAmount"]] = scaler.fit_transform(
    df[["Quantity", "UnitPrice", "TotalAmount"]]
)

print("Scaling Completed")

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

print("Preprocessed dataset saved successfully!")