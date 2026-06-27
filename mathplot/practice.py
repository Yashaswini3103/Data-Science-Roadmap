import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")

plt.bar(df["Name"], df["Marks"])

plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()