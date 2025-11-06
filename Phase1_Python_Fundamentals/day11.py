#Exception Handeling
# CaterLeap Café – Exception Handling

def take_order():
    try:
        qty = int(input("Enter quantity: "))
        price = int(input("Enter price per item: "))
        total = qty * price
        print(f"Total amount: ₹{total}")
    except ValueError:
        print(" Please enter valid numbers only!")
    except Exception as e:
        print("Unexpected error:", e)
    finally:
        print(" Order process completed.")

take_order()

# Some modules introduction
# CaterLeap Café – Using Python Modules

import math
import datetime
import random

# Math Module
radius = 7
area = math.pi * math.pow(radius, 2)
print(f"Area of pizza with radius {radius}cm: {round(area, 2)} sq.cm")

# Datetime Module
current_time = datetime.datetime.now()
print(f"Current Date & Time: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")

# Random Module
special_offer = random.choice(["10% Off", "Buy 1 Get 1", "Free Dessert"])
print(f"Today’s Special Offer: {special_offer}")

