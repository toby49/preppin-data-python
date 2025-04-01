# preppin-data-python
This repository documents my solutions to the Preppin' Data challenges as I learn and practice Python. 

# Preppin' Data Challenge - Week 1

## Summary

This challenge involved cleaning and transforming a dataset using Python and pandas. Key tasks included splitting columns, changing data types, and filtering the data based on conditions.

### Steps Taken:
1. **Read Data**: Loaded the dataset using `pd.read_csv()`.
2. **Split `Flight Details`**: Used `str.split('//', expand=True)` to separate the `Flight Details` column into multiple columns.
3. **Split `Route`**: Separated the `Route` column into `From` and `To` using `str.split('-')`.
4. **Change Data Types**: Converted `Date` to datetime and `Price` to numeric using `pd.to_datetime()` and `pd.to_numeric()`.
5. **Merge Data**: Combined the split columns with the original data using `pd.concat()`.
6. **Replace Values**: Replaced `1`/`0` values in `Flow Card?` with `'Yes'`/`'No'` using `replace()`.
7. **Filter Data**: Created two separate tables for Flow Card holders and non-holders.

### Key Techniques:
- **Data Splitting**: `str.split()`
- **Data Type Conversion**: `pd.to_datetime()`, `pd.to_numeric()`
- **Data Merging**: `pd.concat()`
- **Conditional Filtering**: `df[df['column'] == value]`