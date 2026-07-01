import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="E-Commerce Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 E-Commerce Customer Analytics Dashboard")

# Load Dataset
@st.cache_data
def load_data():
    df = pd.read_csv("data/processed/cleaned_data.csv")

    df["TotalAmount"] = df["Quantity"] * df["UnitPrice"]
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
    df["InvoiceYear"] = df["InvoiceDate"].dt.year

    return df

try:
    df = load_data()

    st.success("Dataset loaded successfully!")

    # KPI Section
    st.header("📈 Project Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Records", f"{len(df):,}")
    col2.metric("Unique Customers", df["CustomerID"].nunique())
    col3.metric("Countries", df["Country"].nunique())

    st.divider()

    # Customer Analysis
    st.header("🏆 Top 10 Customers By Spending")

    customer_sales = (
        df.groupby("CustomerID")["TotalAmount"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    st.dataframe(customer_sales)

    st.divider()

    # Product Analysis
    st.header("📦 Top 10 Products")

    top_products = (
        df.groupby("Description")["Quantity"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    st.dataframe(top_products)

    st.divider()

    # Sales Trend
    st.header("📉 Sales Trend")

    yearly_sales = (
        df.groupby("InvoiceYear")["TotalAmount"]
        .sum()
        .sort_index()
    )

    fig, ax = plt.subplots(figsize=(8, 4))

    ax.plot(
        yearly_sales.index,
        yearly_sales.values,
        marker="o"
    )

    ax.set_title("Sales Trend By Year")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sales")

    st.pyplot(fig)

    st.divider()

    # Customer Segmentation
    st.header("👥 Customer Segmentation")

    customer_total = (
        df.groupby("CustomerID")["TotalAmount"]
        .sum()
    )

    premium = len(customer_total[customer_total > 100])
    regular = len(
        customer_total[
            (customer_total > 50)
            & (customer_total <= 100)
        ]
    )
    basic = len(customer_total[customer_total <= 50])

    seg_df = pd.DataFrame({
        "Segment": ["Premium", "Regular", "Basic"],
        "Customers": [premium, regular, basic]
    })

    st.dataframe(seg_df)

    st.bar_chart(
        seg_df.set_index("Segment")
    )

except Exception as e:
    st.error(f"Error: {e}")