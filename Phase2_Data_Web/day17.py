# day17_data_cleaning
# Data cleaning: missing values, duplicates, renaming columns

import pandas as pd

# sample data (if you have CSV, replace this by pd.read_csv("file.csv"))
data = {
    "Item": ["Paneer", "Biryani", "Noodles", None, "Paneer"],
    "Price": [180, 150, None, 100, 180],
    "Sold": [50, 60, 20, 10, 50]
}
df = pd.DataFrame(data)
print("Original:\n", df)

# 1. Drop rows where Item is missing
df = df.dropna(subset=["Item"])
# 2. Fill missing prices with mean price
df["Price"].fillna(df["Price"].mean(), inplace=True)
# 3. Remove exact duplicate rows
df = df.drop_duplicates()
# 4. Rename columns to standard names
df.rename(columns={"Sold": "Quantity_Sold"}, inplace=True)

print("\nCleaned:\n", df)

# Save cleaned CSV
df.to_csv("cleaned_menu.csv", index=False)
print("\nSaved cleaned_menu.csv")
