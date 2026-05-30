import pandas as pd
import pyodbc
import numpy as np

print("\nStarting SQL Load...\n")

# =========================
# LOAD CSV
# =========================
model_path = r"D:\Desktop\Electric_Vehicle\feature_engineering\EV_Model_FE.csv"
india_path = r"D:\Desktop\Electric_Vehicle\feature_engineering\EV_India_FE.csv"

model_df = pd.read_csv(model_path)
india_df = pd.read_csv(india_path)

print("CSV Files Loaded")

# =========================
# CLEAN DATA (IMPORTANT FIX)
# =========================

# Replace NaN safely
model_df = model_df.replace({np.nan: None})
india_df = india_df.replace({np.nan: None})

# Ensure numeric columns are clean
'''num_cols = ["Electric_Range", "Base_MSRP", "Vehicle_Age"]

for col in num_cols:
    model_df[col] = pd.to_numeric(model_df[col], errors="coerce").fillna(0)'''

# =========================
# SQL CONNECTION
# =========================
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=Hari6104\\MSSQLSERVER1;"
    "DATABASE=EV_Database;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

print("Connected to SQL Server")

# =========================
# LOAD EV_Model_FE
# =========================
cursor.execute("SELECT COUNT(*) FROM EV_Model_FE")
model_count = cursor.fetchone()[0]

if model_count == 0:

    for _, row in model_df.iterrows():

        cursor.execute("""
            INSERT INTO EV_Model_FE (
                Vehicle_ID,
                Model_Year,
                Brand,
                Model,
                Electric_Vehicle_Type,
                CAFV_Eligibility,
                Electric_Range,
                Base_MSRP,
                Vehicle_Age,
                Price_Category,
                Range_Category,
                Vehicle_Type
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        row["Vehicle_ID"],
        row["Model_Year"],
        row["Brand"],
        row["Model"],
        row["Electric_Vehicle_Type"],
        row["CAFV_Eligibility"],
        row["Electric_Range"],
        row["Base_MSRP"],
        row["Vehicle_Age"],
        row["Price_Category"],
        row["Range_Category"],
        row["Vehicle_Type"]
        )

    print("EV_Model_FE Loaded")

else:
    print("EV_Model_FE already has data")

# =========================
# LOAD EV_India_FE
# =========================
cursor.execute("SELECT COUNT(*) FROM EV_India_FE")
india_count = cursor.fetchone()[0]

if india_count == 0:

    for _, row in india_df.iterrows():

        cursor.execute("""
            INSERT INTO EV_India_FE (
                Vehicle_ID,
                Country,
                City,
                State,
                Postal_Code,
                Region,
                Metro_Flag
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        row["Vehicle_ID"],
        row["Country"],
        row["City"],
        row["State"],
        row["Postal_Code"],
        row["Region"],
        row["Metro_Flag"]
        )

    print("EV_India_FE Loaded")

else:
    print("EV_India_FE already has data")

# =========================
# COMMIT
# =========================
conn.commit()
cursor.close()
conn.close()

print("Connection Closed - Load Completed Successfully")