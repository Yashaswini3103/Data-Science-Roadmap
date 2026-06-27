import pandas as pd

df = pd.read_csv("employees.csv")

print(df)
print(df.isnull())
print(df.isnull().sum())
print(df.dropna())
print(df.fillna(0))