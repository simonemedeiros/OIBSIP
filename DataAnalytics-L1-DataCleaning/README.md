# Data Cleaning — Animal Dataset

## Overview

This project demonstrates a structured data cleaning workflow using Python, pandas, and NumPy.

The original dataset contains animal observations with information about species, country, physical measurements, gender, geographic coordinates, observation dates, and data collectors.

The dataset was intentionally inconsistent and was cleaned to produce an analysis-ready version.

## Dataset

* **Source:** `data/raw/animal_data_dirty1.csv`
* **Original records:** 1,011
* **Original columns:** 11
* **Cleaned dataset:** `data/processed/animal_data_cleaned.csv`

## Cleaning Workflow

### 1. Data Quality Assessment

The initial assessment examined:

* Missing values
* Duplicate rows
* Data types
* Unique values
* Numeric distributions
* Potential value anomalies

### 2. Missing Data Handling

Missing values were handled according to the type and context of each variable.

* Categorical variables: mode imputation
* Numeric variables: median imputation
* Geographic coordinates: median imputation where appropriate
* `Animal name`: retained as missing because the field is largely unavailable
* `Animal code`: excluded because the column contained 100% missing values

### 3. Duplicate Removal

Duplicate rows were identified and removed.

* Original rows: 1,011
* Duplicate rows identified: 167
* Rows after duplicate removal: 844

### 4. Standardisation

Inconsistent categorical values were standardised, including:

* Animal type spelling variations
* Country names and country codes
* Inconsistent country values associated with geographic coordinates
* Mixed observation date formats

`Observation date` was converted to a datetime format.

### 5. Outlier Detection

The IQR method was used to identify statistical outliers in numeric variables.

Extreme values were investigated before treatment.

Clearly invalid values, such as negative weights and negative body lengths, were converted to missing values rather than automatically removed.

Other statistical outliers were retained when they could represent legitimate differences between animal species.

### 6. Data Type Correction

Final data types were aligned with the meaning of each variable:

* Text fields → `string`
* Measurements → `float64`
* Geographic coordinates → `float64`
* Observation dates → `datetime`

## Project Structure

```text
DataAnalytics-L1-DataCleaning/
├── data/
│   ├── raw/
│   │   └── animal_data_dirty1.csv
│   └── processed/
│       └── animal_data_cleaned.csv
├── notebooks/
│   └── animal_data_cleaning.ipynb
├── download_data.py
├── requirements.txt
└── README.md
```

## Technologies

* Python
* pandas
* NumPy
* Matplotlib
* Jupyter Notebook

## Output

The cleaned dataset is saved as:

`data/processed/animal_data_cleaned.csv`

The notebook documents the cleaning decisions and validation steps performed throughout the workflow.
