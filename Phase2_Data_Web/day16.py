# ----------------------------
# Day 16 – DataFrame Operations & CSV Handling
# ----------------------------
import pandas as pd

# Create DataFrame
data = {
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "Paneer_Butter_Masala": [1200, 1100, 1300, 1250, 1400],
    "Veg_Biryani": [800, 850, 900, 950, 1000],
    "Gobi_Manchurian": [950, 1000, 1050, 1100, 1200]
}

df = pd.DataFrame(data)
print("Restaurant Sales Data:\n", df)

# Save to CSV
df.to_csv("restaurant_sales.csv", index=False)
print("\nData saved to restaurant_sales.csv")

# Read from CSV
sales_df = pd.read_csv("restaurant_sales.csv")
print("\nRead from CSV:\n", sales_df)

# Basic operations
print("\nTotal sales per day:\n", sales_df.sum(axis=1))
print("\nAverage sales per item:\n", sales_df.mean())

# Sorting
sorted_df = sales_df.sort_values(by="Paneer_Butter_Masala", ascending=False)
print("\nSorted by Paneer Butter Masala sales:\n", sorted_df)

# Grouping example
menu = pd.DataFrame({
    "Category": ["Main", "Main", "Starter", "Starter"],
    "Item": ["Paneer Butter Masala", "Veg Biryani", "Gobi Manchurian", "Veg Soup"],
    "Price": [180, 150, 130, 100]
})
print("\nGrouped by Category (Average Price):\n", menu.groupby("Category")["Price"].mean())
