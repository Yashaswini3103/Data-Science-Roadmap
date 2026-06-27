import pandas as pd

data = {
    "Name": ["Asha", "Rahul", "Priya", "Kiran"],
    "Marks": [85, 90, 78, 95]
}

df = pd.DataFrame(data)
print(df["Name"])
print(df["Marks"])
print("Highest marks:", df["Marks"].max())
print("Lowest marks:", df["Marks"].min())
print("Average marks:", df["Marks"].mean())

print("marks>80:", df[df["Marks"] > 80])