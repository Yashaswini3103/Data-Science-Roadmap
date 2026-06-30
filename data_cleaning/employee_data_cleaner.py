import pandas as pd

df=pd.read_csv("employees_data.csv")

print("Original Data:")
print(df)

print("\nMissing values:")
print(df.isnull().sum())

df = df.fillna(0)
df=df.drop_duplicates()
df=df.rename(columns={'Salary': 'Monthly_Salary'})

print("\nCleaned Data:")
print(df)

df.to_csv("cleaned_employees.csv", index=False)
print("\nFile saved successfully!")