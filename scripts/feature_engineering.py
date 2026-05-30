# ==========================================
# EV FEATURE ENGINEERING PIPELINE
# ==========================================
import pandas as pd
import os
from datetime import datetime

# ------------------------------------------
# Paths
# ------------------------------------------
input_folder = r"D:\Desktop\Electric_Vehicle\cleaned_data"
output_folder = r"D:\Desktop\Electric_Vehicle\feature_engineering"

os.makedirs(output_folder, exist_ok=True)

current_year = datetime.now().year

print("\nStarting Feature Engineering...\n")

# ==========================================
# EV MODEL FEATURE ENGINEERING
# ==========================================

model_df = pd.read_csv(
    os.path.join(
        input_folder,
        "EV_Model_Cleaned.csv"
    )
)

# ------------------------------------------
# Standardize Column Names
# ------------------------------------------
model_df.columns = (
    model_df.columns
    .str.strip()
    .str.replace(" ", "_")
)

print("EV_Model Columns:")
print(model_df.columns.tolist())

# ------------------------------------------
# Vehicle Age
# ------------------------------------------
if "Model_Year" in model_df.columns:

    model_df["Vehicle_Age"] = (
        current_year - model_df["Model_Year"]
    )

# ------------------------------------------
# Price Category
# ------------------------------------------
def price_category(price):

    if price < 1500000:
        return "Budget"

    elif price < 3000000:
        return "Midrange"

    else:
        return "Premium"

if "Base_MSRP" in model_df.columns:

    model_df["Price_Category"] = (
        model_df["Base_MSRP"]
        .apply(price_category)
    )

# ------------------------------------------
# Range Category
# ------------------------------------------
def range_category(rng):

    if rng < 200:
        return "Short"

    elif rng < 400:
        return "Medium"

    else:
        return "Long"

if "Electric_Range" in model_df.columns:

    model_df["Range_Category"] = (
        model_df["Electric_Range"]
        .apply(range_category)
    )

# ------------------------------------------
# Vehicle Type
# ------------------------------------------

two_wheelers = [
    "450X",
    "S1 Pro",
    "Iqube"
]

four_wheelers = [
    "Atto 3",
    "Nexon Ev",
    "Xuv400",
    "Kona Ev",
    "Zs Ev"
]

def vehicle_type(model):

    if model in two_wheelers:
        return "2 Wheeler"

    elif model in four_wheelers:
        return "4 Wheeler"

    else:
        return "Other"

if "Model" in model_df.columns:

    model_df["Vehicle_Type"] = (
        model_df["Model"]
        .apply(vehicle_type)
    )

# ------------------------------------------
# Save EV_Model_FE
# ------------------------------------------
model_df.to_csv(

    os.path.join(
        output_folder,
        "EV_Model_FE.csv"
    ),

    index=False

)

print("EV_Model Feature Engineering Completed")

# ==========================================
# EV INDIA FEATURE ENGINEERING
# ==========================================

india_df = pd.read_csv(
    os.path.join(
        input_folder,
        "EV_India_Cleaned.csv"
    )
)

# ------------------------------------------
# Standardize Column Names
# ------------------------------------------
india_df.columns = (
    india_df.columns
    .str.strip()
    .str.replace(" ", "_")
)

print("\nEV_India Columns:")
print(india_df.columns.tolist())

# ------------------------------------------
# Region Mapping
# ------------------------------------------
region_map = {

    "Tamil Nadu": "South",
    "Karnataka": "South",
    "Kerala": "South",
    "Telangana": "South",
    "Andhra Pradesh": "South",

    "Delhi": "North",
    "Punjab": "North",
    "Haryana": "North",
    "Uttar Pradesh": "North",

    "Maharashtra": "West",
    "Gujarat": "West",
    "Rajasthan": "West",

    "West Bengal": "East",
    "Odisha": "East",
    "Bihar": "East"
}

if "State" in india_df.columns:

    india_df["Region"] = (
        india_df["State"]
        .map(region_map)
    )

# ------------------------------------------
# Metro Flag
# ------------------------------------------
metro_cities = [

    "Chennai",
    "Mumbai",
    "Delhi",
    "Bangalore",
    "Hyderabad"
]

if "City" in india_df.columns:

    india_df["Metro_Flag"] = (
        india_df["City"]
        .isin(metro_cities)
        .astype(int)
    )

# ------------------------------------------
# Ensure Metro_Flag is only 0/1
# ------------------------------------------
if "Metro_Flag" in india_df.columns:

    india_df["Metro_Flag"] = (
        india_df["Metro_Flag"]
        .fillna(0)
        .astype(int)
    )

# ------------------------------------------
# Save EV_India_FE
# ------------------------------------------
india_df.to_csv(

    os.path.join(
        output_folder,
        "EV_India_FE.csv"
    ),

    index=False

)

print("EV_India Feature Engineering Completed")

# ==========================================
# FINAL MESSAGE
# ==========================================

print("\nFeature Engineering Completed Successfully")

