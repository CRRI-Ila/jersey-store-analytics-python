# Jersey Store Sales Profitability Analysis

## Project Overview

This project performs a structured data analysis of a retail jersey store dataset to identify profitability patterns across products (players). The dataset contained inconsistencies including duplicate records, missing values, and non-numeric entries, requiring systematic cleaning before analysis.

The primary objective of this project was to design a clear data-processing pipeline that transforms raw transaction data into meaningful business insights using Python.

This project demonstrates practical skills in data preprocessing, algorithmic computation, feature engineering, and analytical visualization — all relevant to Computer Engineering problem-solving and structured system design.

---

## Problem Statement

Retail datasets often contain noisy and incomplete data. Without proper cleaning and validation, financial analysis can produce incorrect conclusions.

The goal of this project was to:

- Clean and standardize a raw sales dataset
- Recalculate revenue to eliminate potential human calculation errors
- Identify the most and least profitable players
- Analyze purchasing patterns such as bulk orders and discount impact
- Present findings clearly using visualizations

---

## Dataset Description

The dataset consists of jersey sales transactions including:

- Player name
- Jersey size
- Quantity purchased
- Unit price
- Discount applied
- Revenue

Because the dataset was uncleaned, several preprocessing steps were necessary before analysis.

---

## Methodology

<img width="909" height="1039" alt="image" src="https://github.com/user-attachments/assets/98fe3a4c-39f6-4fd7-af9d-1988538ff32a" />

### 1. Data Cleaning

The following cleaning steps were implemented:

- Removed duplicate transaction records to prevent inflated revenue calculations
- Converted the `Quantity` column to numeric format
- Replaced missing quantity values using the median (robust against outliers)
- Filled missing categorical values (e.g., jersey size) with a default value
- Recomputed revenue using a standardized formula:

Revenue = (Price × Quantity) − Discount

Recomputing revenue ensured consistency and prevented reliance on potentially incorrect stored values.

---

### 2. Feature Engineering

To enhance analysis, additional features were created:

- **HighQuantity Flag**: Identifies bulk purchases (Quantity ≥ 3)
- **TotalDiscount**: Captures the total discount applied per order
- Aggregated total revenue by player

These transformations enabled deeper insight into profitability drivers.

---

### 3. Profitability Analysis

Using group-by aggregation, total revenue was calculated per player.

This allowed identification of:

- The most profitable player (highest total revenue)

<img width="751" height="184" alt="image" src="https://github.com/user-attachments/assets/a476b81b-027d-42bf-b9d4-013016d74740" />


- The least profitable player (lowest total revenue)

<img width="650" height="155" alt="image" src="https://github.com/user-attachments/assets/203c127c-3b4b-449f-adee-679107ffbbb0" />


The results highlight how purchasing patterns and discount structures impact revenue distribution.

---

### 4. Data Visualization

Multiple visualizations were generated to support interpretation:

- Bar chart of total revenue per player

<img width="945" height="258" alt="image" src="https://github.com/user-attachments/assets/c574e8c6-e73f-4026-a080-419124cd3120" />

  
- Pie chart of quantity distribution

<img width="1261" height="265" alt="image" src="https://github.com/user-attachments/assets/b57e0f54-9cf9-4e58-9ceb-d0e52f2e83ff" />

  
- Bar chart of jersey size distribution

<img width="764" height="268" alt="image" src="https://github.com/user-attachments/assets/6059bd8a-a414-4311-b072-8cbcaf241f9c" />

  
- Scatter plot of total quantity sold vs price per player

<img width="789" height="565" alt="image" src="https://github.com/user-attachments/assets/93ca9e34-31ef-4a00-a060-57c20e405a3d" />

  
- Bar chart of high-quantity orders

<img width="825" height="271" alt="image" src="https://github.com/user-attachments/assets/7ae90cd1-16c7-4fd3-afe5-baed18be1942" />

  
- Bar chart of total discount applied per player

  <img width="1036" height="250" alt="image" src="https://github.com/user-attachments/assets/7f4640db-0852-499a-aff6-23a52289a8f4" />


Visualizations improve interpretability and simulate real-world business reporting.


---

## Key Findings

- Revenue distribution was uneven across players, indicating demand concentration.
- Bulk purchases contributed significantly to total revenue.
- Discount levels influenced profitability margins.
- Data cleaning substantially affected revenue calculations, demonstrating the importance of preprocessing in analytical workflows.

---

## Technical Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Google Colab (development environment)

---
## How to Run
1. Install dependencies:
2. Run the script:
Alternatively, open the notebook in Google Colab and execute all cells.
## Engineering Relevance

Although this project focuses on retail analytics, it demonstrates key Computing skills:

- Structured data pipeline design  
- Algorithmic computation  
- Modular code organization  
- Validation and debugging of real-world data  
- Logical transformation of inputs into measurable outputs  

The workflow mirrors engineering system design:

Raw Data → Cleaning → Transformation → Analysis → Output Visualization  

This structured approach reflects systematic problem-solving principles used in engineering disciplines.

---

## Future Improvements

Potential enhancements include:

- adding a lattest Report automatically
- Automating report generation  
- Adding statistical analysis (variance, correlation)  
- Implementing command-line execution  
- Expanding to predictive modeling  
- Deploying as a simple web dashboard  
