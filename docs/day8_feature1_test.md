# Day 8 - Core Feature 1 Testing

## Feature: Customer Purchase Analysis

### Test 1: Normal Dataset

* Input: Original cleaned dataset
* Expected Result: Top customers displayed correctly
* Actual Result: Passed

### Test 2: Empty Dataset

* Input: Empty dataframe
* Expected Result: Display "Dataset is empty."
* Actual Result: Passed

### Test 3: Missing CustomerID Column

* Input: Dataset without CustomerID column
* Expected Result: Display "CustomerID column missing."
* Actual Result: Passed

### Test 4: Missing TotalAmount Column

* Input: Dataset without TotalAmount column
* Expected Result: Display "TotalAmount column missing."
* Actual Result: Passed

### Test 5: Large Dataset

* Input: Full e-commerce dataset
* Expected Result: Top customers displayed without errors
* Actual Result: Passed

## Conclusion

The Customer Purchase Analysis feature was tested under normal and edge-case scenarios and performed successfully in all cases.
