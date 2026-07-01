import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------------
# PAGE CONFIG
# ----------------------------------

st.set_page_config(
    page_title="E-Commerce Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 E-Commerce Customer Analytics Dashboard")
st.markdown("Analyze customer purchases, product performance, and sales trends.")

# ----------------------------------
# LOAD DATASET
# ----------------------------------

@st.cache_data
def load_data():
    try:
        df = pd.read_csv(
            "data/data.csv",
            encoding="ISO-8859-1"
        )

        df["TotalAmount"] = (
            df["Quantity"] * df["UnitPrice"]
        )

        df["InvoiceDate"] = pd.to_datetime(
            df["InvoiceDate"]
        )

        df["InvoiceYear"] = (
            df["InvoiceDate"].dt.year
        )

        return df

    except Exception as e:
        st.error(f"Dataset loading failed: {e}")
        return pd.DataFrame()


df = load_data()

if df.empty:
    st.stop()

st.success("Dataset loaded successfully!")

# ----------------------------------
# PROJECT OVERVIEW
# ----------------------------------

st.header("📈 Project Overview")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Records",
    f"{len(df):,}"
)

col2.metric(
    "Unique Customers",
    df["CustomerID"].nunique()
)

col3.metric(
    "Countries",
    df["Country"].nunique()
)

st.divider()

# ----------------------------------
# DATA PREVIEW
# ----------------------------------

st.header("📄 Dataset Preview")

st.dataframe(
    df.head(10),
    use_container_width=True
)

st.divider()

# ----------------------------------
# TOP CUSTOMERS
# ----------------------------------

st.header("🏆 Top 10 Customers By Spending")

customer_sales = (
    df.groupby("CustomerID")["TotalAmount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

st.dataframe(
    customer_sales,
    use_container_width=True
)

st.bar_chart(customer_sales)

st.divider()

# ----------------------------------
# TOP PRODUCTS
# ----------------------------------

st.header("📦 Top 10 Products")

top_products = (
    df.groupby("Description")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

st.dataframe(
    top_products,
    use_container_width=True
)

st.bar_chart(top_products)

st.divider()

# ----------------------------------
# SALES TREND
# ----------------------------------

st.header("📉 Sales Trend Analysis")

yearly_sales = (
    df.groupby("InvoiceYear")["TotalAmount"]
    .sum()
    .sort_index()
)

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(
    yearly_sales.index,
    yearly_sales.values,
    marker="o"
)

ax.set_title("Sales Trend By Year")
ax.set_xlabel("Year")
ax.set_ylabel("Total Sales")
ax.grid(True)

st.pyplot(fig)

st.divider()

# ----------------------------------
# CUSTOMER SEGMENTATION
# ----------------------------------

st.header("👥 Customer Segmentation")

customer_total = (
    df.groupby("CustomerID")["TotalAmount"]
    .sum()
)

premium = len(
    customer_total[
        customer_total > 100
    ]
)

regular = len(
    customer_total[
        (customer_total > 50)
        & (customer_total <= 100)
    ]
)

basic = len(
    customer_total[
        customer_total <= 50
    ]
)

segment_df = pd.DataFrame({
    "Segment": [
        "Premium",
        "Regular",
        "Basic"
    ],
    "Customers": [
        premium,
        regular,
        basic
    ]
})

st.dataframe(
    segment_df,
    use_container_width=True
)

st.bar_chart(
    segment_df.set_index("Segment")
)

st.divider()

# ----------------------------------
# USER-FRIENDLY HELP SECTION
# ----------------------------------

with st.expander("ℹ️ How to Use This Dashboard"):
    st.write("""
    • Project Overview shows key business metrics.

    • Top Customers identifies highest spending customers.

    • Top Products shows best-selling products.

    • Sales Trend visualizes revenue growth over time.

    • Customer Segmentation groups customers into Premium,
      Regular, and Basic categories.
    """)

# ----------------------------------
# FOOTER
# ----------------------------------

st.markdown("---")
st.markdown(
    "**E-Commerce Customer Analytics Dashboard** | "
    "Built using Python, Pandas, Matplotlib, and Streamlit"
)