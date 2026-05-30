
drop table if exists EV_India_FE
drop table if exists EV_Model_FE


CREATE TABLE EV_Model_FE (
    DOL_Vehicle_ID        BIGINT NOT NULL,
    Model_Year            INT NULL,
    Brand                 VARCHAR(100) NULL,
    Model                 VARCHAR(150) NULL,
    Electric_Vehicle_Type VARCHAR(100) NULL,
    CAFV_Eligibility      VARCHAR(100) NULL,

    Electric_Range        INT NULL,
    Base_MSRP             BIGINT NULL,
    Vehicle_Age           INT NULL,

    Price_Category        VARCHAR(50) NULL,
    Range_Category        VARCHAR(50) NULL,
    Vehicle_Type          VARCHAR(50) NULL
);


CREATE TABLE EV_India_FE (
    DOL_Vehicle_ID   BIGINT NOT NULL,
    Country          VARCHAR(50) NULL,
    City             VARCHAR(100) NULL,
    State            VARCHAR(100) NULL,
    Postal_Code      VARCHAR(20) NULL,

    Region           VARCHAR(50) NULL,
    Metro_Flag       BIT NULL
);



-- Data Understanding

-- View data

SELECT * FROM EV_Model_FE;

SELECT * FROM EV_India_FE;

-- total vehicles

SELECT COUNT(*) AS Total_Vehicles
FROM EV_Model_FE;

-- distinct brands

SELECT DISTINCT Brand
FROM EV_Model_FE;

-- Unique vehicle types

SELECT DISTINCT Vehicle_Type
FROM EV_Model_FE;

-- Average electric range

SELECT
    AVG(Electric_Range) AS Avg_Range
FROM EV_Model_FE;

-- Premium Vehicles count

SELECT
    Price_Category,
    COUNT(*) AS Total
FROM EV_Model_FE
GROUP BY Price_Category;

-- Average electric range

SELECT
    AVG(Electric_Range) AS Average_Range
FROM EV_Model_FE;

-- Metro and Non-metro

SELECT
    Metro_Flag,
    COUNT(*) AS Total
FROM EV_India_FE
GROUP BY Metro_Flag;


-- Business Problem Analysis

-- Which brands dominate EV market?

SELECT
    Brand,
    COUNT(*) AS Total_Vehicles
FROM EV_Model_FE
GROUP BY Brand
ORDER BY Total_Vehicles DESC;

-- Which region has highest EV adoption?

SELECT Region, COUNT(*) AS Total_EV
FROM EV_India_FE
GROUP BY Region
ORDER BY Total_EV DESC;

-- Which states are leading EV adoption?

SELECT State, COUNT(*) AS Total_EV
FROM EV_India_FE
GROUP BY State
ORDER BY Total_EV DESC;

-- Premium vs budget EVs

SELECT
    Price_Category,
    COUNT(*) AS Total
FROM EV_Model_FE
GROUP BY Price_Category;

-- Which EV model is most used?

SELECT Model, COUNT(*) AS Total
FROM EV_Model_FE
GROUP BY Model
ORDER BY Total DESC;

-- which vehicle type is popular?

SELECT
    Vehicle_Type,
    COUNT(*) AS Total
FROM EV_Model_FE
GROUP BY Vehicle_Type;

-- -- Which brands offer highest range?

SELECT
    Brand,
    AVG(Electric_Range) AS Avg_Range
FROM EV_Model_FE
GROUP BY Brand
ORDER BY Avg_Range DESC;

-- How many EVs are Budget/Midrange/Premium?

SELECT Price_Category,
       COUNT(*) AS Total
FROM EV_Model_FE
GROUP BY Price_Category;

-- Which brand sells the most premium EVs?

SELECT Brand,
       COUNT(*) AS Premium_Count
FROM EV_Model_FE
WHERE Price_Category = 'Premium'
GROUP BY Brand
ORDER BY Premium_Count DESC;

-- Which brand provides highest average range?

SELECT Brand,
       AVG(Electric_Range) AS Avg_Range
FROM EV_Model_FE
GROUP BY Brand
ORDER BY Avg_Range DESC;

-- Range category distribution

SELECT Range_Category,
       COUNT(*) AS Total
FROM EV_Model_FE
GROUP BY Range_Category;

-- which state buys the most premium EVs?

SELECT 
    ROUND(
        100.0 * SUM(CASE WHEN Price_Category = 'Premium' THEN 1 ELSE 0 END)
        / COUNT(*), 2
    ) AS Premium_Percentage
FROM EV_Model_FE;

-- Which brands dominate metro cities?

SELECT M.Brand,
       COUNT(*) AS Total
FROM EV_Model_FE M
JOIN EV_India_FE I
ON M.DOL_Vehicle_ID = I.DOL_Vehicle_ID
WHERE I.Metro_Flag = 1
GROUP BY M.Brand
ORDER BY Total DESC;

-- Average EV range by state

SELECT I.State,
       AVG(M.Electric_Range) AS Avg_Range
FROM EV_Model_FE M
JOIN EV_India_FE I
ON M.DOL_Vehicle_ID = I.DOL_Vehicle_ID
GROUP BY I.State
ORDER BY Avg_Range DESC;

-- Premium vs budget by state

SELECT I.State, M.Price_Category, COUNT(*) AS Total
FROM EV_Model_FE M
JOIN EV_India_FE I
ON M.DOL_Vehicle_ID = I.DOL_Vehicle_ID
GROUP BY I.State, M.Price_Category




