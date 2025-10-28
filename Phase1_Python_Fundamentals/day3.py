#Dictionaries!!!


# Create a dictionary for a catering menu item
menu_item = {
    "name": "Paneer Butter Masala",
    "price": 180,
    "ingredients": ["Paneer", "Butter", "Tomato", "Cream"]
}

print("Menu Item:", menu_item)

print("Dish name:", menu_item["name"])
print("Price:", menu_item["price"])

# Modify price
menu_item["price"] = 200
print("Updated price:", menu_item["price"])

# Add a new key-value pair
menu_item["category"] = "Main Course"
print("Updated Menu Item:", menu_item)


#exercise 1:

menu_item = {
    "name": "Veg Biryani",
    "price": 250,
    "ingredients": ["Rice", "Vegetables", "Spices"]
}

print(f"Today's Special: {menu_item['name']}")
print(f"Price: ₹{menu_item['price']}")
print("Ingredients:")
for ingredient in menu_item["ingredients"]:
    print("-", ingredient)
