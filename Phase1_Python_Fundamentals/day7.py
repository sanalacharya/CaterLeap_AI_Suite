#Step 5 – File I/O (Input and Output in Python)

# Creating a new file and writing data into it
file = open("menu.txt", "w", encoding="utf-8")  # Added encoding
file.write("Welcome to CaterLeap Café\n")
file.write("Today's Specials:\n")
file.write("1. Paneer Butter Masala - ₹180\n")
file.write("2. Veg Biryani - ₹150\n")
file.close()

print("File created and data written successfully!")


# Reading content from a file
file = open("menu.txt", "r")  # 'r' = read mode
data = file.read()
file.close()

print("File Content:\n")
print(data)


