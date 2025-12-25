import pandas as pd
#step 1:Read the csv file
df=pd.read_csv('employees.csv')
#Step 2:inspect the data 
print("first 5 rows of the dataset :")
print(df.head())
print("\n last 5 rows of the dataset :")
print(df.tail())
print("\n data types:")
print(df.dtypes)
#Step 3:Summary statistics 
print("\n summary statistics:")
print(df.describe())
print("\n Mean")
print(df.mean(numeric_only=True))
print("\n Median")
print(df.median(numeric_only=True))
print("\n mimimum")
print(df.min(numeric_only=True))
print("\n maximum")
print(df.max(numeric_only=True))
#Step 4:filtering rows where age>25
filtered_rows=df[df['Age']>25]
print("\n rows where age>25:")
print(filtered_rows)
#Step 5 select specific columns 
selected_columns=df[["Name","Age","Salary"]]
print("\n selected columns:")
print(selected_columns)
#step 6 slice subset 
subset=df.iloc[0:3,0:3]
print("\n subset of the data:")
print(subset)
#step 7 save filtered results 
filtered_rows.to_csv('filtered_employees.csv',index=False)
filtered_rows.to_excel('filtered_employees.xlsx',index=False)
print("\n filtered data saved to 'filtered_employees.csv' and 'filtered_employees.xlsx'")