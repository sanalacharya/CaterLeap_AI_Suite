# ----------------------------------------
# Phase 2:  Pandas Fundamentals
# ----------------------------------------

import pandas as pd

# --- Create Series ---
sales = pd.Series([1200, 1100, 1300, 1250, 1400], index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri'])
print("\nSales Series:\n", sales)

# --- Create DataFrame ---
data = {
    "Name": ["Sanal", "Arjun", "Diya"],
    "Age": [21, 22, 20],
    "Course": ["AI", "CSE", "IT"]
}
df = pd.DataFrame(data)
print("\nStudent DataFrame:\n", df)

# ---  Access & Filter Data ---
print("\nNames:\n", df["Name"])
print("\nAge > 20:\n", df[df["Age"] > 20])

# ---  Add, Update, Delete Columns ---
df["Marks"] = [85, 90, 88]
df["Age"] = df["Age"] + 1
df.drop("Marks", axis=1, inplace=True)
print("\nAfter Column Operations:\n", df)

# --- Summary & Statistics ---
print("\nDescribe:\n", df.describe(include='all'))
print("Mean Age:", df["Age"].mean())

# ---  CSV Handling ---
df.to_csv("students.csv", index=False)
read_df = pd.read_csv("students.csv")
print("\nRead CSV Data:\n", read_df)

# --- Sorting & Filtering ---
sorted_df = df.sort_values(by="Age", ascending=False)
print("\nSorted by Age:\n", sorted_df)

# ---  Grouping & Aggregation ---
marks_data = {
    "Course": ["AI", "CSE", "AI", "IT", "CSE"],
    "Marks": [85, 90, 80, 75, 95]
}
marks_df = pd.DataFrame(marks_data)
print("\nAverage Marks per Course:\n", marks_df.groupby("Course")["Marks"].mean())

# ---  Missing Data Handling ---
data2 = {
    "Name": ["Sanal", "Arjun", "Diya"],
    "Age": [21, None, 20],
    "Marks": [85, 90, None]
}
df2 = pd.DataFrame(data2)
df2["Age"].fillna(df2["Age"].mean(), inplace=True)
df2.dropna(subset=["Marks"], inplace=True)
print("\nAfter Handling Missing Data:\n", df2)

# --- Merge / Combine DataFrames ---
df1 = pd.DataFrame({"ID": [1, 2], "Name": ["Sanal", "Arjun"]})
df2 = pd.DataFrame({"ID": [1, 2], "Marks": [85, 90]})
merged = pd.merge(df1, df2, on="ID")
print("\nMerged DataFrame:\n", merged)

# ---  Export to Excel ---
merged.to_excel("merged_data.xlsx", index=False)
print("\nData exported to Excel successfully!")
