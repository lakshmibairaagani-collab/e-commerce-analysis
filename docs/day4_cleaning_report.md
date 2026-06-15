# Day 4 Data Cleaning Report

## Missing Values Handling

* Description column had 1,454 missing values.

* Missing descriptions were filled with "Unknown".

* CustomerID column had 135,080 missing values.

* Missing CustomerID values were filled with 0.

## Duplicate Rows

* Total duplicate rows found: 5,268
* Duplicate rows were removed successfully.

## Data Type Corrections

* InvoiceDate converted to DateTime format.
* CustomerID converted to Integer format.

## Dataset Summary

* Original Records: 541,909
* Records After Cleaning: 536,641

## Output File

Cleaned dataset saved as:

data/processed/cleaned_data.csv
