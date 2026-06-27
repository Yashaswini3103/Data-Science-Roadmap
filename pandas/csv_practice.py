import pandas as pd

df = pd.read_csv("students.csv")

print(df)
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())

print("Average Marks:", df["Marks"].mean())


print("students with marks>80:")
print(df[df["Marks"] > 80])
print("students with marks<80:")
print(df[df["Marks"] < 80])

print(df["Name"])

print(df["Age"])