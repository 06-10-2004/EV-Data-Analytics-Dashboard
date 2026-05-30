import streamlit as st
import pandas as pd
import pyodbc
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="EV Dashboard", layout="wide")

# =========================
# SQL CONNECTION
# =========================
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=Hari6104\\MSSQLSERVER1;"
    "DATABASE=EV_Database;"
    "Trusted_Connection=yes;"
)
def run_query(query):
    return pd.read_sql(query, conn)
# =========================
# SIDEBAR NAVIGATION
# =========================
page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Data Analysis",
        "Business Analysis"
    ]
)
# ==========================================================
# HOME PAGE
# ==========================================================
if page == "Home":

    st.title("EV Data Analytics Dashboard")
    st.markdown("### End-to-End Electric Vehicle Market Analysis (India)")

    st.divider()

    # ======================================================
    # PROJECT OVERVIEW
    # ======================================================
    st.subheader("Project Overview")

    st.write("""
    This project is an end-to-end Electric Vehicle (EV) Data Analytics Dashboard
    developed using Python, SQL Server, and Streamlit.

    The project analyzes EV adoption patterns in India using:
    - Data Cleaning
    - Feature Engineering
    - SQL Analysis
    - Interactive Dashboard Visualization

    The project follows the ETL pipeline:
    Extract → Transform → Load
    """)

    # ======================================================
    # BUSINESS PROBLEM
    # ======================================================
    st.subheader("Business Problem")

    st.write("""
    The main objective of this project is to analyze Electric Vehicle (EV)
    adoption patterns in India and understand how the EV market is growing
    across different regions and vehicle categories.

    The project focuses on identifying which EV brands are dominating the market,
    which states show higher EV adoption, and how electric range and 
    vehicle types vary across the dataset.

    Using SQL analysis and interactive visualizations, the dashboard helps
    understand overall EV market trends and regional distribution patterns.
    """)

    # ======================================================
    # TOOLS USED
    # ======================================================
    st.subheader("Tools Used")

    st.write("""
    - Python
    - Pandas
    - NumPy
    - SQL Server
    - PyODBC
    - Streamlit
    - Matplotlib
    - Seaborn
    """)

    # ======================================================
    # DATASETS
    # ======================================================
    st.subheader("Datasets")

    st.write("""
    Dataset Source: Kaggle Website

    Raw Datasets:
    - EV_Model.csv
    - EV_India.csv

    Feature Engineered Datasets:
    - EV_Model_FE
    - EV_India_FE
    """)

    # ======================================================
    # PROJECT STRUCTURE
    # ======================================================
    st.subheader("Project Folder Structure")

    st.code("""
Electric_Vehicle/
│
├── cleaned_data/
│   ├── EV_India_Cleaned.csv
│   └── EV_Model_Cleaned.csv
│
├── EV_Datasets/
│   ├── EV_Model.csv
│   └── EV_India.csv
│
├── feature_engineering/
│   ├── EV_India_FE.csv
│   └── EV_Model_FE.csv
│
├── SQL-DB/
│
├── scripts/
│   ├── data_cleaning.py
│   ├── feature_engineering.py
│   ├── Validation.py
│   ├── loading_to_SQL.py
│   └── Streamlit_App.py
│
├── Virtualenv/
│
└── README.md
    """)

    # ======================================================
    # FOLDER EXPLANATION
    # ======================================================
    st.subheader("Folder Explanation")

    st.write("""
    - EV_Datasets → Stores raw datasets downloaded from Kaggle

    - cleaned_data → Stores cleaned CSV files after preprocessing

    - feature_engineering → Stores transformed datasets with newly created features

    - SQL-DB → Contains SQL tables and analysis queries

    - scripts → Contains Python scripts for cleaning, feature engineering,
      validation, SQL loading, and dashboard creation

    - Virtualenv → Stores project dependencies and environment packages

    - README.md → Contains project documentation
    """)

    # ======================================================
    # SAMPLE DATA
    # ======================================================
    st.subheader("Sample Data")

    st.markdown("**EV_Model_FE (Top 5)**")
    st.dataframe(
        run_query("SELECT TOP 5 * FROM EV_Model_FE")
    )

    st.markdown("**EV_India_FE (Top 5)**")

    df = run_query(
        "SELECT TOP 5 * FROM EV_India_FE"
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    # ======================================================
    # VISUALIZATIONS USED
    # ======================================================
    st.subheader("Visualizations Used")

    st.write("""
    - KPI Metrics
    - Bar Charts
    - Pie Charts
    - Comparative Analysis Charts
    """)

    # ======================================================
    # USE OF PROJECT
    # ======================================================
    st.subheader("Use of This Project")

    st.write("""
    This project analyzes Electric Vehicle adoption patterns in India using
    data visualization and SQL-based analytics. It helps understand EV trends
    such as brand performance, pricing distribution, regional adoption,
    vehicle categories, and electric range patterns through interactive dashboards.
    """)

    # ======================================================
    # CAVEATS
    # ======================================================
    st.subheader("Caveats")

    st.write("""
    - Range values are approximate
    - This is not a real-time dataset
    - Brand and model mappings are not fully realistic
    
    Example:
    - Ola Electric → 450X
    - Byd India → Xuv400
    - Ather Energy → Zs Ev
    - Tata Motors → S1 Pro
    """)

    # ======================================================
    # FUTURE ENHANCEMENTS
    # ======================================================
    st.subheader("Future Enhancements")

    st.write("""
    - Add logging system for pipeline tracking
    - Implement advanced ETL pipeline automation
    - Add machine learning models for:
        - EV adoption prediction
        - Price prediction
    """)

# ==========================================================
# DATA UNDERSTANDING + BUSINESS ANALYSIS
# ==========================================================

elif page == "Data Analysis":

    st.header("Data Understanding Overview")

    # ======================================================
    # KPI ROW
    # ======================================================
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)

    df_total = run_query("SELECT COUNT(*) AS Total FROM EV_Model_FE")
    total_ev = df_total["Total"][0] if df_total is not None else 0
    kpi1.metric("Total EVs", total_ev)

    df_avg = run_query("SELECT AVG(Electric_Range) AS Avg_Range FROM EV_Model_FE")
    avg_range = df_avg["Avg_Range"][0]
    kpi2.metric("Avg Range", f"{avg_range:.2f} km" if avg_range else "0 km")

    df_brand = run_query("SELECT COUNT(DISTINCT Brand) AS Brands FROM EV_Model_FE")
    kpi3.metric("Total Brands", df_brand["Brands"][0])

    df_type = run_query("SELECT COUNT(DISTINCT Vehicle_Type) AS Types FROM EV_Model_FE")
    kpi4.metric("Vehicle Types", df_type["Types"][0])

    st.divider()

    # ======================================================
    # Helper function → ADD VALUE LABELS ON BARS
    # ======================================================
    def add_labels(ax):
        for container in ax.containers:
            ax.bar_label(container, fontsize=7, padding=2)

    # ======================================================
    # ROW 1
    # ======================================================
    col1, col2 = st.columns(2)

    df1 = run_query("""
        SELECT Brand, COUNT(*) AS Total
        FROM EV_Model_FE
        GROUP BY Brand
        ORDER BY Total DESC
    """).head(8)

    with col1:
        if not df1.empty:
            fig, ax = plt.subplots(figsize=(4, 2.6))
            sns.barplot(data=df1, y="Brand", x="Total", ax=ax)
            ax.set_title("Top Brands")
            add_labels(ax)
            st.pyplot(fig)

    df2 = run_query("""
        SELECT Vehicle_Type, COUNT(*) AS Total
        FROM EV_Model_FE
        GROUP BY Vehicle_Type
    """)

    with col2:
        if not df2.empty:
            fig, ax = plt.subplots(figsize=(4, 2.6))
            sns.barplot(data=df2, x="Vehicle_Type", y="Total", ax=ax)
            ax.set_title("Vehicle Types")
            add_labels(ax)
            plt.xticks(rotation=45)
            st.pyplot(fig)

    # ======================================================
    # ROW 2
    # ======================================================
    col3, col4 = st.columns(2)

    # ======================================================
    # REGION EV ADOPTION
    # ======================================================
    df5 = run_query("""
        SELECT Region, COUNT(*) AS Total_EV
        FROM EV_India_FE
        GROUP BY Region
    """)

    with col3:
        if not df5.empty:
            fig, ax = plt.subplots(figsize=(4, 2.6))

            sns.barplot(
                data=df5,
                x="Region",
                y="Total_EV",
                ax=ax
            )

            ax.set_title("Region EV Adoption")

            add_labels(ax)

            plt.xticks(rotation=45)

            st.pyplot(fig)

    # ======================================================
    # TOP STATES
    # ======================================================
    df6 = run_query("""
        SELECT TOP 5 State, COUNT(*) AS Total_EV
        FROM EV_India_FE
        GROUP BY State
        ORDER BY Total_EV DESC
    """)

    with col4:
        if not df6.empty:
            fig, ax = plt.subplots(figsize=(4, 2.6))

            sns.barplot(
                data=df6,
                y="State",
                x="Total_EV",
                ax=ax
            )

            ax.set_title("Top States")

            add_labels(ax)

            st.pyplot(fig)

# ==========================================================
# BUSINESS ANALYSIS PAGE (FIXED + LABELS)
# ==========================================================

elif page == "Business Analysis":

    st.header("Business Analysis Overview")

    # ======================================================
    # SAFE KPI FUNCTION
    # ======================================================
    def safe_value(df, col):
        try:
            val = df[col][0]
            return 0 if val is None else val
        except:
            return 0

    k1, k2 = st.columns(2)

    df_k1 = run_query("SELECT AVG(Electric_Range) AS Avg_Range FROM EV_Model_FE")
    avg_range = safe_value(df_k1, "Avg_Range")
    k1.metric("⚡ Avg Range", f"{avg_range:.1f} km")

    df_k2 = run_query("""
        SELECT
            COUNT(*) * 100.0 / NULLIF((SELECT COUNT(*) FROM EV_Model_FE),0)
            AS Premium_Pct
        FROM EV_Model_FE
        WHERE Price_Category = 'Premium'
    """)
    premium_pct = safe_value(df_k2, "Premium_Pct")
    k2.metric("Premium EVs", f"{premium_pct:.1f}%")

    st.divider()

    # ======================================================
    # ADD LABEL FUNCTION (IMPORTANT FIX)
    # ======================================================
    def add_labels(ax):
        for container in ax.containers:
            ax.bar_label(container, fontsize=7, padding=2)

    # ======================================================
    # ROW 1
    # ======================================================
    c1, c2 = st.columns(2)

    df12 = run_query("""
        SELECT Brand, AVG(Electric_Range) AS Avg_Range
        FROM EV_Model_FE
        GROUP BY Brand
        ORDER BY Avg_Range DESC
    """).head(5)

    with c1:
        if not df12.empty:
            fig, ax = plt.subplots(figsize=(4, 2.6))
            sns.barplot(data=df12, y="Brand", x="Avg_Range", ax=ax)
            ax.set_title("Brand Avg Range")
            add_labels(ax)
            st.pyplot(fig)

    df13 = run_query("""
        SELECT Price_Category, COUNT(*) AS Total
        FROM EV_Model_FE
        GROUP BY Price_Category
    """)

    with c2:
        if not df13.empty:
            fig, ax = plt.subplots(figsize=(4, 2.6))
            sns.barplot(data=df13, x="Price_Category", y="Total", ax=ax)
            ax.set_title("EV Price Segmentation")
            add_labels(ax)
            st.pyplot(fig)

    # ======================================================
    # ROW 2
    # ======================================================
    c3, c4 = st.columns(2)

    df14 = run_query("""
        SELECT TOP 5 State, COUNT(*) AS Premium_Count
        FROM EV_Model_FE M
        JOIN EV_India_FE I ON M.Vehicle_ID = I.Vehicle_ID
        WHERE Price_Category = 'Premium'
        GROUP BY State
        ORDER BY Premium_Count DESC
    """)

    with c3:
        if not df14.empty:
            fig, ax = plt.subplots(figsize=(4, 2.6))
            sns.barplot(data=df14, y="State", x="Premium_Count", ax=ax)
            ax.set_title("Premium EV States")
            add_labels(ax)
            st.pyplot(fig)

    df17 = run_query("""
        SELECT TOP 5 M.Brand, COUNT(*) AS Total
        FROM EV_Model_FE M
        JOIN EV_India_FE I ON M.Vehicle_ID = I.Vehicle_ID
        WHERE I.Metro_Flag = 1
        GROUP BY M.Brand
        ORDER BY Total DESC
    """)

    with c4:
        if not df17.empty:
            fig, ax = plt.subplots(figsize=(4, 2.6))
            sns.barplot(data=df17, y="Brand", x="Total", ax=ax)
            ax.set_title("Metro Market Brands")
            add_labels(ax)
            st.pyplot(fig)

    # ======================================================
    # ROW 3
    # ======================================================
    c5, c6 = st.columns(2)

    df18 = run_query("""
        SELECT TOP 5 State, AVG(Electric_Range) AS Avg_Range
        FROM EV_Model_FE M
        JOIN EV_India_FE I ON M.Vehicle_ID = I.Vehicle_ID
        GROUP BY State
        ORDER BY Avg_Range DESC
    """)

    with c5:
        if not df18.empty:
            fig, ax = plt.subplots(figsize=(4, 2.6))
            sns.barplot(data=df18, y="State", x="Avg_Range", ax=ax)
            ax.set_title("Range by State")
            add_labels(ax)
            st.pyplot(fig)

    df19 = run_query("""
        SELECT Range_Category, COUNT(*) AS Total
        FROM EV_Model_FE
        GROUP BY Range_Category
    """)

    with c6:
        if not df19.empty:
            fig, ax = plt.subplots(figsize=(4, 2.6))
            sns.barplot(data=df19, x="Range_Category", y="Total", ax=ax)
            ax.set_title("EV Range Categories")
            add_labels(ax)
            st.pyplot(fig)

    # ======================================================
    # ROW 4
    # ======================================================
    c7, c8 = st.columns(2)

    # ======================================================
    # STATE VS EV PRICING
    # ======================================================
    df20 = run_query("""
        SELECT TOP 10 State, Price_Category, COUNT(*) AS Total
        FROM EV_Model_FE M
        JOIN EV_India_FE I
        ON M.Vehicle_ID = I.Vehicle_ID
        GROUP BY State, Price_Category
        ORDER BY Total DESC
    """)

    with c7:

        if not df20.empty:

            fig, ax = plt.subplots(figsize=(4, 2.6))

            sns.barplot(
                data=df20,
                x="State",
                y="Total",
                hue="Price_Category",
                ax=ax
            )

            ax.set_title("State vs EV Pricing")

            plt.xticks(rotation=45)

            for container in ax.containers:
                ax.bar_label(
                    container,
                    fontsize=7,
                    padding=6,
                    label_type="edge"
                )

            ax.legend(
                title="Price Category",
                fontsize=7
            )

            st.pyplot(fig)

    # ======================================================
    # METRO VS NON-METRO
    # ======================================================
    df4 = run_query("""
        SELECT Metro_Flag, COUNT(*) AS Total
        FROM EV_India_FE
        GROUP BY Metro_Flag
    """)

    # Convert safely into integer
    df4["Metro_Flag"] = (
        df4["Metro_Flag"]
        .astype(int)
    )

    # Create labels
    df4["Metro_Label"] = (
        df4["Metro_Flag"]
        .map({
            1: "Metro",
            0: "Non-Metro"
        })
    )

    with c8:

        if not df4.empty:
            fig, ax = plt.subplots(figsize=(4, 2.6))

            ax.pie(
                df4["Total"],
                labels=df4["Metro_Label"],
                autopct="%1.1f%%",
                startangle=90
            )

            ax.set_title("Metro vs Non-Metro")

            ax.axis("equal")

            st.pyplot(fig)