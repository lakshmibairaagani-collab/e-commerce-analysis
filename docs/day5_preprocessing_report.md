# Day 5 Preprocessing Report

## Derived Features Created

1. TotalAmount = Quantity × UnitPrice
2. InvoiceYear = Year extracted from InvoiceDate

## Encoding

* Applied One-Hot Encoding to the Country column.

## Scaling

Applied StandardScaler to:

* Quantity
* UnitPrice
* TotalAmount

## Train-Test Split

* Training Set: 429,312 records (80%)
* Testing Set: 107,329 records (20%)

## Output

Preprocessed dataset saved successfully as:

data/processed/preprocessed_data.csv
