# day18_merge_pivot.py
# Merge/concat/pivot examples with Pandas

import pandas as pd

menu = pd.DataFrame({
    "Item": ["Paneer", "Biryani", "Noodles"],
    "Price": [180, 150, 120]
})

sales = pd.DataFrame({
    "Item": ["Paneer", "Biryani", "Paneer", "Noodles"],
    "Day": ["Mon", "Mon", "Tue", "Tue"],
    "Qty": [10, 8, 12, 5]
})

# Merge menu + sales on Item
merged = pd.merge(sales, menu, on="Item")
print("Merged:\n", merged)

# Pivot: total qty per item per day
pivot = merged.pivot_table(values="Qty", index="Item", columns="Day", aggfunc="sum", fill_value=0)
print("\nPivot table:\n", pivot)

# Concat example: append another day's sales
more_sales = pd.DataFrame({"Item":["Biryani"], "Day":["Tue"], "Qty":[7]})
concat_all = pd.concat([sales, more_sales], ignore_index=True)
print("\nConcatenated sales:\n", concat_all)

# Save summary
pivot.to_csv("sales_pivot_summary.csv")
print("\nSaved sales_pivot_summary.csv")
