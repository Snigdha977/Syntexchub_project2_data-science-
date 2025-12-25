# Syntexchub_project2_data-science-
Its my internship project for week 1 and its entirely based on data analysis and data operations using pandas 
# Pandas CSV Reader & Basic Analysis

## Project Overview
This project demonstrates basic data analysis using the pandas library.
A sample CSV and Excel dataset is loaded, inspected, analyzed, and processed
to perform common data operations.

## Tools & Technologies
- Python
- pandas
- openpyxl

## Tasks Performed
- Loaded CSV and Excel files into a pandas DataFrame
- Inspected data using head, tail, and data types
- Computed summary statistics (mean, median, min, max, count)
- Filtered rows based on conditions
- Selected specific columns and created subsets
- Saved processed data to CSV and Excel files

## Files Included
- employees.csv
- employees.xlsx
- pandas_analysis.py
- filtered_employees.csv
- filtered_employees.xlsx

## Outcome
The project successfully completes all required operations and demonstrates
foundational pandas skills for data analysis.
## Output 
first 5 rows of the dataset :
     Name  Age  Department  Salary  Experience
0   Aarav   22          IT   30000           1
1   Sneha   28          HR   45000           4
2   Rohan   35     Finance   60000           8
3  Ananya   26          IT   40000           3
4  Vikram   42  Management   80000          15

 last 5 rows of the dataset :
     Name  Age  Department  Salary  Experience
0   Aarav   22          IT   30000           1
1   Sneha   28          HR   45000           4
2   Rohan   35     Finance   60000           8
3  Ananya   26          IT   40000           3
4  Vikram   42  Management   80000          15

 data types:
Name          object
Age            int64
Department    object
Salary         int64
Experience     int64
dtype: object

 summary statistics:
             Age       Salary  Experience
count   5.000000      5.00000    5.000000
mean   30.600000  51000.00000    6.200000
std     7.924645  19493.58869    5.540758
min    22.000000  30000.00000    1.000000
25%    26.000000  40000.00000    3.000000
50%    28.000000  45000.00000    4.000000
75%    35.000000  60000.00000    8.000000
max    42.000000  80000.00000   15.000000

 Mean
Age              30.6
Salary        51000.0
Experience        6.2
dtype: float64

 Median
Age              28.0
Salary        45000.0
Experience        4.0
dtype: float64

 mimimum
Age              22
Salary        30000
Experience        1
dtype: int64

 maximum
Age              42
Salary        80000
Experience       15
dtype: int64

 rows where age>25:
     Name  Age  Department  Salary  Experience
1   Sneha   28          HR   45000           4
2   Rohan   35     Finance   60000           8
3  Ananya   26          IT   40000           3
4  Vikram   42  Management   80000          15

 selected columns:
     Name  Age  Salary
0   Aarav   22   30000
1   Sneha   28   45000
2   Rohan   35   60000
3  Ananya   26   40000
4  Vikram   42   80000

 subset of the data:
    Name  Age Department
0  Aarav   22         IT
1  Sneha   28         HR
2  Rohan   35    Finance

 filtered data saved to 'filtered_employees.csv' and 'filtered_employees.xlsx'

C:\Users\snigd\OneDrive\Documents\Syntexchub_project2_data-science-\Syntexchub_project2_data-science->
