import pandas as pd

df=pd.read_csv("employees_data.csv")

print(df)
print(df.isnull().sum())
print(df.fillna(0))
print(df.drop_duplicates())
df=df.rename(columns={'Salary': 'Monthly_Salary'})
df.to_csv("cleaned_employees.csv", index=False)