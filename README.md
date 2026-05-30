
# EV Market India – Data Pipeline & Analytics Dashboard
PPT LINK ---> https://github.com/06-10-2004/EV_Market_India/blob/main/Electric%20Vehicle%20In%20India.pdf
---

This project analyzes Electric Vehicle (EV) adoption trends in India using a complete data pipeline and an interactive analytics dashboard. The system processes raw EV datasets, performs data cleaning and feature engineering, stores the data in a structured SQL database, and visualizes key insights using a Streamlit dashboard.

---

#### Project Objective

The objective of this project is to build an end-to-end ETL[Extract, Transform, Load] data pipeline that processes EV market data and provides meaningful insights through visual analytics via production level Streamlit Dashboard webapp.

---

#### Tools and Technologies Used

- Python
- Pandas
- Logging, Time, Sys, OS
- SQL Server
- Matplotlib
- Seaborn
- Streamlit
- Git & GitHub

---

#### Business Problem

The rapid growth of Electric Vehicles requires better understanding of regional adoption trends, price affordability, battery range demand, and infrastructure gaps. Without proper analysis, policymakers and companies cannot effectively plan EV infrastructure or market strategies.

---

#### Data Pipeline Architecture

The project follows a structured ETL pipeline:

1. Data Extraction from EV datasets
2. Data Cleaning and Validation to handle missing values and inconsistencies
3. Feature Engineering to create additional analytical variables
4. Loading processed data into a SQL Data Warehouse star schema
5. Visualization through a production level Streamlit dashboard

---

#### Project Organization and Purpose

The project is organized into multiple modules to manage different stages of the data pipeline including data cleaning, feature engineering, database loading, and visualization.

---

#### Data Analysis and Insights

The Streamlit dashboard provides visual analysis including:

- EV adoption by region
- Metro vs Non-Metro adoption comparison
- EV price distribution
- EV range analysis
- Premium vs non-premium EV comparison
- States with lowest EV adoption
- EV price trends over time

---

#### Key Insights and Business Impact

| Insight | Value / Observation |
|-------|----------------------|
| Non-Metro areas account for most adoption | 82.1% of EVs are in Non-Metro areas → need for infrastructure expansion |
| South India leads adoption; East India lags | South: 51,995 vehicles, East: 26,033 vehicles |
| Average EV price: ₹45 lakh (affordability barrier) | High prices highlight affordability issues |
| Battery range demand balanced (High / Medium / Low) | High: 33.8%, Medium: 33.8%, Low: 32.4% |
| States with low adoption indicate infrastructure gaps | Delhi: 4,143; Kerala: 8,217; Andhra Pradesh: 8,528 |

---

#### Future Enhancements

- Predictive Modeling:
Use machine learning to forecast EV adoption
trends by region or state
- Computer Vision:
Analyze images of EV models for features, design, or safety
compliance
=======
# EV Data Analytics Dashboard – End-to-End Electric Vehicle Market Analysis (India)

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red.svg)
![SQL Server](https://img.shields.io/badge/Database-SQL%20Server-orange.svg)
![Status](https://img.shields.io/badge/Project-Completed-green.svg)

---

## Project Overview

The EV Data Analytics Dashboard is an end-to-end data analytics project built using Python, SQL Server, and Streamlit. It analyzes electric vehicle adoption trends in India using structured datasets and provides actionable business insights through data processing, SQL analysis, and interactive visualizations.

The project follows a complete analytics pipeline:

Extract → Transform → Validate → Load

---

## Business Problem

The Indian electric vehicle market is expanding rapidly, creating a need to understand:

- EV adoption patterns across regions  
- Leading EV manufacturers  
- Vehicle type preferences  
- Pricing segment distribution  
- EV range usage trends  
- Regional adoption differences  

The objective is to convert raw EV data into meaningful insights for business decision-making.

---

## Technology Stack

| Category | Tools |
|----------|------|
| Programming Language | Python |
| Data Processing | Pandas |
| Database | SQL Server |
| Connectivity | PyODBC |
| Visualization | Matplotlib, Seaborn |
| Dashboard | Streamlit |
| Version Control | Git, GitHub |

---

## ETL Workflow

Extract → Transform → Validate → Load

### Extract
- Load raw EV datasets from CSV files

### Transform
- Data cleaning  
- Handling missing values  
- Standardization  
- Feature engineering  

### Validate
- Duplicate checks  
- Null value checks  
- Data consistency validation  

### Load
- Load processed data into SQL Server  
- Perform SQL-based analysis  

---

## Datasets

### EV_Model.csv
Contains EV specifications:
- Brand  
- Model  
- Vehicle Type  
- Battery Capacity  
- EV Range  
- Base Price  

### EV_India.csv
Contains EV adoption data:
- State  
- City  
- Vehicle Type  
- Registration Count  
- Adoption Distribution  

---

## Project Structure

```text
Electric_Vehicle/
│
├── EV_Datasets/
│   ├── EV_Model.csv
│   ├── EV_India.csv
│
├── cleaned_data/
│   ├── EV_Model_Cleaned.csv
│   ├── EV_India_Cleaned.csv
│
├── feature_engineering/
│   ├── EV_Model_FE.csv
│   ├── EV_India_FE.csv
│
├── SQL-DB/
│   ├── SQL_Query_Analysis.sql
│
├── scripts/
│   ├── data_cleaning.py
│   ├── feature_engineering.py
│   ├── validation.py
│   ├── loading_to_SQL.py
│   ├── Streamlit_App.py
│
├── Presentation/
│
└── README.md
```

---

## Dashboard Features

### Data Cleaning
- Missing value handling  
- Duplicate removal  
- Data standardization  

### Feature Engineering
- Price segmentation  
- EV range categorization  
- Regional grouping  

### SQL Analysis
- Brand performance analysis  
- Regional EV distribution  
- Vehicle type analysis  
- Pricing trends  

### Streamlit Dashboard
- KPI cards  
- Interactive charts  
- Comparative analysis  
- Business insights visualization  

---

## Key Insights

| Metric | Value |
|--------|------|
| Total EVs | 51,066 |
| Total Brands | 8 |
| Vehicle Types | 2 |
| Average EV Range | 298 km |

### Insights

- Tata Motors is the leading EV brand  
- South India shows highest EV adoption  
- Non-metro regions account for majority EV usage  
- Mid-range and premium EVs dominate the market  
- Medium-range EVs are most preferred  

---

## Installation

### Clone Repository

git clone https://github.com/06-10-2004/EV-Data-Analytics-Dashboard.git

---

### Navigate to Project Folder

cd EV-Data-Analytics-Dashboard

---

### Create Virtual Environment

python -m venv venv

---

### Activate Virtual Environment

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate

---

### Install Dependencies

pip install -r requirements.txt

---

If requirements.txt is not available:

pip install pandas numpy streamlit matplotlib seaborn pyodbc

---

## How to Run

### Run Data Pipeline

python scripts/data_cleaning.py  
python scripts/feature_engineering.py  
python scripts/validation.py  
python scripts/loading_to_SQL.py  

---

### Run Streamlit Dashboard

streamlit run scripts/Streamlit_App.py  

---

## Future Enhancements

- Automated ETL pipeline  
- Logging framework  
- EV adoption prediction model  
- EV price prediction model  
- Cloud deployment  
- Advanced BI dashboards  

---

## Caveats

- Dataset is not real-time  
- brand–model mappings are not fully realistic  
- EV range values are approximate  
- Analysis is limited to available dataset  
- Results are for educational purposes  

---

## Conclusion

This project demonstrates a complete end-to-end data analytics workflow using Python, SQL Server, and Streamlit.

It covers:
- Data cleaning  
- Feature engineering  
- SQL analysis  
- Data visualization  
- Dashboard development  

It provides meaningful insights into the Indian EV market and serves as a strong portfolio project for data analytics roles.

---

## Author

HARITHA S

Data Analyst | Python | SQL | Streamlit | Data Visualization

