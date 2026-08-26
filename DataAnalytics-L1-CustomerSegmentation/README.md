# Oasis Infobyte Data Analytics

## Project Overview
This repository contains the project for Exploratory Data Analysis (EDA) on Retail Sales Data

The objective of this project is to perform a thorough exploratory data analysis on a retail sales dataset to uncover pattterns, customer behavior trends, and actionable business insights using Python and standard data science libraries.

---

## Repository Structure

OIBSIP/
├--DataAnalytics-L1-CustomerSegmentation/
│   ├── notebooks/
│   │   └── retail-sales-dataset.ipynb
│   ├── download_data.py
│   └── README.md

## Tech Stack
* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Jupyter Notebook

## Feature Checklist
- [x] Load dataset and perform initial inspection: shape, column dtypes, null value check
- [x] Descriptive statistics: mean, median, mode, standard deviation for all numerical columns
- [x] Time series analysis: plot monthly and quarterly sales trends using line charts
- [x] Customer demographics analysis: distribution of customer age groups, gender breakdown
- [x] Product analysis: top 10 best-selling products; revenue by product category (bar chart)
- [x] Heatmap: correlation matrix between numerical variables
- [x] At least one additional visualisation of your choice that reveals a non-obvious insight (Sales Channel vs. Payment Method)
- [x] Markdown cells throughout the notebook with written observations after each chart
- [x] Conclusion section: at least 3 specific, actionable business recommendations based on findings

## Summary of Insights and Findings
1. **Sales Trends:** Analysis of monthly and quarterly transaction records highlights significant revenue volatility, including a sharp decline in Q2 followed by recovery phases.
2. **Category Performance:** While product quantities sold remain consistent, category-level financials reveal that the Beauty category generates the highest overall revenue compared to other segments.
3. **Pricing and Channels:** Correlation matrices and categorical visualisations indicate that transaction amounts remain stable across different sales channels and payment methods, while promotional discounts operate independently of overall transaction scale.

## Business Recommendations
1. **Optimize Marketing Allocation:** Shift advertising budgets toward top-performing revenue categories like Beauty to maximize return on investment.
2. **Restructure Promotional Pricing:** Replace static discounting with volume-based or tiered promotional pricing models to effectively stimulate transaction scale.
3. **Mitigate Seasonal Fluctuations:** Investigate operational bottlenecks during low-performing quarters to ensure consistent revenue stabilization throughout the year.
