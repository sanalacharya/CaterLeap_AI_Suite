# Appending new items to the menu file
file = open("menu.txt", "a", encoding="utf-8")  # Added encoding
file.write("3. Gobi Manchurian - ₹130\n")
file.write("4. Butter Naan - ₹50\n")
file.close()

print("New items added to the menu successfully!")


# Using with open() automatically closes the file
with open("menu.txt", "r") as file:
    for line in file:
        print(line.strip())


