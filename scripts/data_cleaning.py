# ==========================================
# EV DATA CLEANING PIPELINE (FINAL VERSION)
# ==========================================

import pandas as pd
import os

# ------------------------------------------
# Paths
# ------------------------------------------
input_folder = r"D:\Desktop\Electric_Vehicle\EV_Datasets"
output_folder = r"D:\Desktop\Electric_Vehicle\cleaned_data"

os.makedirs(output_folder, exist_ok=True)

print("\nStarting EV Data Cleaning...\n")

# ==========================================
# EV INDIA CLEANING
# ==========================================

city_df = pd.read_csv(
    os.path.join(input_folder, "EV_India.csv")
)

print("EV_India Original Shape:", city_df.shape)

# ------------------------------------------
# Standardize Column Names
# ------------------------------------------
city_df.columns = (
    city_df.columns
    .str.strip()
    .str.replace(" ", "_")
)

# ------------------------------------------
# Rename Columns
# ------------------------------------------
city_df.rename(
    columns={
        "County": "Country",
        "DOL_Vehicle_ID": "Vehicle_ID"
    },
    inplace=True
)

# ------------------------------------------
# Remove Unwanted Column
# ------------------------------------------
city_df.drop(
    columns=["Vehicle_Location"],
    errors="ignore",
    inplace=True
)

# ------------------------------------------
# Standardize Text Columns
# ------------------------------------------
for col in ["State", "City", "Country"]:

    if col in city_df.columns:

        city_df[col] = (
            city_df[col]
            .astype(str)
            .str.strip()
            .str.title()
        )

# ------------------------------------------
# Remove Duplicates
# ------------------------------------------
city_df.drop_duplicates(inplace=True)

# ------------------------------------------
# Remove Missing Vehicle IDs
# ------------------------------------------
if "Vehicle_ID" in city_df.columns:
    city_df.dropna(
        subset=["Vehicle_ID"],
        inplace=True
    )

print("EV_India Cleaned Shape:", city_df.shape)

# ------------------------------------------
# Save Cleaned EV India Dataset
# ------------------------------------------
city_df.to_csv(
    os.path.join(
        output_folder,
        "EV_India_Cleaned.csv"
    ),
    index=False
)

# ==========================================
# EV MODEL CLEANING
# ==========================================

type_df = pd.read_csv(
    os.path.join(input_folder, "EV_Model.csv")
)

print("\nEV_Model Original Shape:", type_df.shape)

# ------------------------------------------
# Standardize Column Names
# ------------------------------------------
type_df.columns = (
    type_df.columns
    .str.strip()
    .str.replace(" ", "_")
)

# ------------------------------------------
# Rename Columns
# ------------------------------------------
type_df.rename(
    columns={
        "DOL_Vehicle_ID": "Vehicle_ID",
        "Make": "Brand",
        "Price_per_Range": "Price_per_km",
        "Clean_Alternative_Fuel_Vehicle_(CAFV)_Eligibility":
            "CAFV_Eligibility"
    },
    inplace=True
)

print("Standardized Columns:")
print(type_df.columns.tolist())

# ------------------------------------------
# Standardize EV Type Labels
# ------------------------------------------
if "Electric_Vehicle_Type" in type_df.columns:

    type_df["Electric_Vehicle_Type"] = (
        type_df["Electric_Vehicle_Type"]
        .replace({
            "Battery Electric Vehicle (BEV)": "BEV",
            "Plug-in Hybrid Electric Vehicle (PHEV)": "PHEV"
        })
    )

# ------------------------------------------
# Standardize Text Columns
# ------------------------------------------
for col in ["Brand", "Model"]:

    if col in type_df.columns:

        type_df[col] = (
            type_df[col]
            .astype(str)
            .str.strip()
            .str.title()
        )

# ------------------------------------------
# Convert Numeric Columns
# ------------------------------------------
numeric_cols = [
    "Vehicle_ID",
    "Model_Year",
    "Electric_Range",
    "Base_MSRP"
]

for col in numeric_cols:

    if col in type_df.columns:

        type_df[col] = pd.to_numeric(
            type_df[col],
            errors="coerce"
        )

# ------------------------------------------
# Fill Missing Values
# ------------------------------------------
if "Electric_Range" in type_df.columns:

    type_df["Electric_Range"] = (
        type_df["Electric_Range"]
        .fillna(type_df["Electric_Range"].median())
    )

if "Base_MSRP" in type_df.columns:

    type_df["Base_MSRP"] = (
        type_df["Base_MSRP"]
        .fillna(type_df["Base_MSRP"].median())
    )

# ------------------------------------------
# Remove Duplicates
# ------------------------------------------
type_df.drop_duplicates(inplace=True)

# ------------------------------------------
# Remove Missing Vehicle IDs
# ------------------------------------------
if "Vehicle_ID" in type_df.columns:

    type_df.dropna(
        subset=["Vehicle_ID"],
        inplace=True
    )

print("EV_Model Cleaned Shape:", type_df.shape)

# ------------------------------------------
# Save Cleaned EV Model Dataset
# ------------------------------------------
type_df.to_csv(
    os.path.join(
        output_folder,
        "EV_Model_Cleaned.csv"
    ),
    index=False
)

# ==========================================
# FINAL MESSAGE
# ==========================================

print("\nData Cleaning Completed Successfully")