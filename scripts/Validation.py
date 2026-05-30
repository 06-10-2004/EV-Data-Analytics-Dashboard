# ==========================================
# EV DATA VALIDATION PIPELINE (FIXED)
# ==========================================

import pandas as pd
import os

# ------------------------------------------
# Paths
# ------------------------------------------
cleaned_folder = r"D:\Desktop\Electric_Vehicle\cleaned_data"
feature_folder = r"D:\Desktop\Electric_Vehicle\feature_engineering"

print("\nStarting Validation...\n")

# ==========================================
# LOAD CLEANED DATA
# ==========================================

model_cleaned = pd.read_csv(
    os.path.join(cleaned_folder, "EV_Model_Cleaned.csv")
)

india_cleaned = pd.read_csv(
    os.path.join(cleaned_folder, "EV_India_Cleaned.csv")
)


# ==========================================
# VALIDATE CLEANED DATA
# ==========================================

print("\nVALIDATING CLEANED DATA")

print("\nEV_Model_Cleaned Shape:", model_cleaned.shape)
print("EV_India_Cleaned Shape:", india_cleaned.shape)

# Missing values
print("\nEV_Model Missing Values:")
print(model_cleaned.isnull().sum())

print("\nEV_India Missing Values:")
print(india_cleaned.isnull().sum())

# Duplicate check
if "Vehicle_ID" in model_cleaned.columns:
    print("\nEV_Model Duplicate IDs:",
          model_cleaned["Vehicle_ID"].duplicated().sum())

if "Vehicle_ID" in india_cleaned.columns:
    print("EV_India Duplicate IDs:",
          india_cleaned["Vehicle_ID"].duplicated().sum())

# ==========================================
# LOAD FEATURE ENGINEERED DATA
# ==========================================

model_fe = pd.read_csv(
    os.path.join(feature_folder, "EV_Model_FE.csv")
)

india_fe = pd.read_csv(
    os.path.join(feature_folder, "EV_India_FE.csv")
)

# ==========================================
# VALIDATE FEATURE ENGINEERED DATA
# ==========================================

print("\nVALIDATING FEATURE ENGINEERED DATA")

print("\nEV_Model_FE Shape:", model_fe.shape)
print("EV_India_FE Shape:", india_fe.shape)

# Missing values
print("\nEV_Model_FE Missing Values:")
print(model_fe.isnull().sum())

print("\nEV_India_FE Missing Values:")
print(india_fe.isnull().sum())

# Duplicate check
if "Vehicle_ID" in model_fe.columns:
    print("\nEV_Model_FE Duplicate IDs:",
          model_fe["Vehicle_ID"].duplicated().sum())

if "Vehicle_ID" in india_fe.columns:
    print("EV_India_FE Duplicate IDs:",
          india_fe["Vehicle_ID"].duplicated().sum())

# ==========================================
# FINAL MESSAGE
# ==========================================

print("\nValidation Completed Successfully")