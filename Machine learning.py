import pandas as pd
import numpy as np

# 1. Create a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi'],
        'Age': [25, 30, 35, 28, 32, 29, 27, 33],
        'City': ['New York', 'London', 'Paris', 'Tokyo', 'Sydney', 'London', 'New York', 'Paris'],
        'Salary': [50000, 60000, 75000, 55000, 62000, 68000, 71000, 78000],
        'Experience': [2, 5, 10, 3, 6, 4, 2, 8]}
df = pd.DataFrame(data)
print("1. Original DataFrame:")
print(df)
print("\n" + "="*50 + "\n")

# 2. Basic Information and Exploration
print("2. Basic DataFrame Info:")
df.info()
print("\n")
print("3. Descriptive Statistics:")
print(df.describe())
print("\n")
print("4. First 3 rows (head):")
print(df.head(3))
print("\n")
print("5. Last 2 rows (tail):")
print(df.tail(2))
print("\n" + "="*50 + "\n")

# 3. Data Selection and Filtering
print("6. Select 'Name' and 'Age' columns:")
print(df[['Name', 'Age']])
print("\n")
print("7. Filter rows where Age > 30:")
print(df[df['Age'] > 30])
print("\n")
print("8. Select rows with 'City' as 'London' or 'New York':")
print(df[df['City'].isin(['London', 'New York'])])
print("\n" + "="*50 + "\n")

# 4. Handling Missing Values (introduce some missing values for demonstration)
df_with_nan = df.copy()
df_with_nan.loc[2, 'Salary'] = np.nan
df_with_nan.loc[5, 'Experience'] = np.nan
print("9. DataFrame with missing values:")
print(df_with_nan)
print("\n")
print("10. Check for missing values:")
print(df_with_nan.isnull().sum())
print("\n")
print("11. Fill missing 'Salary' with the mean:")
df_with_nan['Salary'].fillna(df_with_nan['Salary'].mean(), inplace=True)
print(df_with_nan)
print("\n")
print("12. Drop rows with any remaining missing values:")
df_cleaned = df_with_nan.dropna()
print(df_cleaned)
print("\n" + "="*50 + "\n")

# 5. Data Manipulation
print("13. Sort DataFrame by 'Salary' in descending order:")
print(df.sort_values(by='Salary', ascending=False))
print("\n")
print("14. Add a new column 'Bonus' (Salary * 0.1):")
df['Bonus'] = df['Salary'] * 0.1
print(df)
print("\n")
print("15. Apply a function to a column (e.g., convert 'City' to uppercase):")
df['City_Upper'] = df['City'].apply(lambda x: x.upper())
print(df)
print("\n")
print("16. Group by 'City' and calculate the mean 'Salary':")
print(df.groupby('City')['Salary'].mean())
print("\n")
print("17. Value counts for 'City':")
print(df['City'].value_counts())
print("\n" + "="*50 + "\n")

# 6. Combining DataFrames (Example)
data2 = {'Name': ['Alice', 'Bob', 'Eve', 'Grace'],
         'Department': ['HR', 'IT', 'Marketing', 'Sales']}
df2 = pd.DataFrame(data2)
print("18. Another DataFrame (df2):")
print(df2)
print("\n")
print("19. Merge df and df2 on 'Name':")
merged_df = pd.merge(df, df2, on='Name', how='inner')
print(merged_df)
print("\n" + "="*50 + "\n")

# 7. Reshaping and Pivoting
print("20. Create a pivot table of average Salary by City and Experience:")
pivot_table_df = df.pivot_table(index='City', values='Salary', aggfunc='mean')
print(pivot_table_df)
print("\n" + "="*50 + "\n")

# 8. Time Series (Example, create a date column)
df['Date'] = pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05', '2023-01-06', '2023-01-07', '2023-01-08'])
df.set_index('Date', inplace=True)
print("21. DataFrame with a datetime index:")
print(df)
print("\n")
print("22. Resample the data by week and calculate the sum of Salary:")
print(df['Salary'].resample('W').sum())
print("\n" + "="*50 + "\n")

# 9. Other Useful Functions
print("23. Drop 'City_Upper' column:")
df.drop('City_Upper', axis=1, inplace=True)
print(df.head())
print("\n")
print("24. Rename 'Experience' column to 'Years_Experience':")
df.rename(columns={'Experience': 'Years_Experience'}, inplace=True)
print(df.head())
print("\n")
print("25. Convert DataFrame to a NumPy array:")
numpy_array = df.to_numpy()
print(numpy_array)
print("\n")
print("26. Save DataFrame to a CSV file (output.csv):")
df.to_csv('output.csv', index=False)
print("DataFrame saved to 'output.csv'")
