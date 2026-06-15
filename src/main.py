import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/data.csv", encoding="latin1")

# Dataset Information
print("Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

# Remove rows with missing descriptions
df = df.dropna(subset=["Description"])

# Chart 1: Quantity Distribution
df["Quantity"].hist()
plt.title("Quantity Distribution")
plt.xlabel("Quantity")
plt.ylabel("Frequency")
plt.show()

# Chart 2: Unit Price Distribution
df["UnitPrice"].hist()
plt.title("Unit Price Distribution")
plt.xlabel("Unit Price")
plt.ylabel("Frequency")
plt.show()

# Chart 3: Top 10 Countries
df["Country"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Countries by Transactions")
plt.xlabel("Country")
plt.ylabel("Transactions")
plt.show()