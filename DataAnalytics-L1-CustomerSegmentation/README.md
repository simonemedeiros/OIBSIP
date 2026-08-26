# Customer Segmentation — Retail Sales Analysis

Exploratory data analysis of a retail sales dataset using Python.

The project focuses on sales performance, customer characteristics, product categories, and transaction patterns.

## Project Structure

```text
OIBSIP/
└── DataAnalytics-L1-CustomerSegmentation/
    ├── notebooks/
    │   └── retail-sales-dataset.i
    ├─outputs 
    ├── download_data.py
    └── README.md
```

## Tools

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Jupyter Notebook

## Analysis

The notebook includes:

* Dataset inspection
* Data types and missing values
* Descriptive statistics
* Monthly and quarterly sales analysis
* Customer age and gender distribution
* Top 10 best-selling products
* Revenue by product category
* Correlation analysis
* Sales channel and payment method analysis
* Data visualisations with observations

## Key Findings

### Sales

Sales vary throughout the analysed periods, with a noticeable decline in Q2 followed by a recovery.

### Product Categories

The **Beauty** category has the highest total revenue among the analysed categories.

### Sales Channels and Payment Methods

Transaction amounts are relatively similar across the different sales channels and payment methods.

### Discounts

The analysis does not show a clear relationship between discount values and transaction amounts.

## Business Recommendations
1. Category Performance: Beauty accounts for the highest revenue, while Clothing has the lowest. This suggests an opportunity to review category-level sales, pricing, and product mix before allocating additional marketing or inventory resources.
2. Promotional Strategy: The weak correlation between discount percentage and transaction amount (-0.09) suggests that discounts alone may not explain changes in transaction value. Testing targeted promotions, such as product bundles or volume-based offers, could provide a clearer view of their impact on sales.
3. Sales Fluctuations: The decline observed in Q2 2025, followed by a recovery later in the year, indicates a need to investigate the factors behind these changes. Comparing product, customer, and transaction-level data across periods could help identify patterns that support future sales planning.

## Notebook

The complete analysis is available in:

`notebooks/retail-sales-dataset.ipynb`

