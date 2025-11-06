<<<<<<< HEAD
# -------------------------------
# CaterLeap Café Manager
# -------------------------------
# Author: Sanal Acharya
# Mentor: Navneeth Sir
# Phase 1: Python Fundamentals
# -------------------------------
=======
# ================================================================
# PROJECT: CaterLeap Café Manager
# OVERALL EXAMPLE – PHASE 1: Python Fundamentals (The Kitchen Prep)
# ---------------------------------------------------------------
# Developer: Sanal Acharya
# Mentor: Navneeth Sir
# Duration: 20 Oct 2025 – 02 Nov 2025
# ---------------------------------------------------------------
# This project demonstrates all key Python fundamentals including:
# Variables & Data Types
# Lists & Dictionaries
# Conditionals
# Functions
# File I/O
# Classes & Objects
# Inheritance
# Exception Handling
# Python Modules (datetime, random)
# ================================================================
>>>>>>> phase-2

import datetime
import random

<<<<<<< HEAD
# 1 Variables, Lists, Dictionaries
=======
# Variables, Lists, Dictionaries
>>>>>>> phase-2
menu = {
    "Paneer Butter Masala": 180,
    "Veg Biryani": 150,
    "Gobi Manchurian": 130,
    "Butter Naan": 50
}
orders = []

<<<<<<< HEAD
# 2 Functions
=======
# Functions
>>>>>>> phase-2
def show_menu():
    """Display available menu items and prices."""
    print("\n----- MENU -----")
    for item, price in menu.items():
        print(f"{item} - ₹{price}")

def take_order():
    """Take order from user with validation."""
    try:
        item = input("\nEnter item name: ").strip()
        if item not in menu:
            raise ValueError("Item not available in menu!")
        qty = int(input("Enter quantity: "))
        if qty <= 0:
            raise ValueError("Quantity must be greater than 0!")
        orders.append((item, qty))
<<<<<<< HEAD
        print(f" Added {qty} × {item}")
=======
        print(f"Added {qty} × {item}")
>>>>>>> phase-2
    except ValueError as e:
        print(f" Error: {e}")
    except Exception as e:
        print(" Unexpected error:", e)

<<<<<<< HEAD
# 3 File I/O
=======
# File I/O
>>>>>>> phase-2
def save_bill(bill_text):
    """Save generated bill to a text file."""
    try:
        with open("bill.txt", "w", encoding="utf-8") as f:
            f.write(bill_text)
        print("\n Bill saved as bill.txt")
    except Exception as e:
        print(" Failed to save bill:", e)

<<<<<<< HEAD
# 4 Classes & Objects
=======
# Classes & Objects
>>>>>>> phase-2
class Bill:
    """Generate and manage customer bill."""
    def __init__(self, orders):
        self.orders = orders
        self.total = 0

    def generate_bill(self):
        print("\n----- BILL -----")
        bill_lines = []
        for item, qty in self.orders:
            price = menu[item] * qty
            self.total += price
            line = f"{item} × {qty} = ₹{price}"
            print(line)
            bill_lines.append(line)

        # Bill Summary
        bill_text = "\n".join(bill_lines)
        bill_text += f"\n---------------------\nTotal = ₹{self.total}"
        bill_text += f"\nDate: {datetime.datetime.now().strftime('%d-%b-%Y %H:%M:%S')}"
        save_bill(bill_text)

<<<<<<< HEAD
# 5 Inheritance
=======
# Inheritance
>>>>>>> phase-2
class DiscountedBill(Bill):
    """Extended Bill class with discount functionality."""
    def __init__(self, orders, discount):
        super().__init__(orders)
        self.discount = discount

    def generate_bill(self):
        super().generate_bill()
        discount_amount = self.total * (self.discount / 100)
        final_total = self.total - discount_amount
        print(f"\nDiscount ({self.discount}%): ₹{discount_amount}")
        print(f"Final Total: ₹{final_total}")

        # Random offer from random module
<<<<<<< HEAD
        offer = random.choice([" Free Dessert", " 5% Off Next Visit", " Free Soup", " Lucky Draw Entry"])
        print(f"\nToday’s Special Offer: {offer}")
        print("\nBill generated on:", datetime.datetime.now().strftime("%d-%b-%Y %H:%M:%S"))
=======
        offer = random.choice([" Free Dessert", "5% Off Next Visit", " Free Soup", " Lucky Draw Entry"])
        print(f"\nToday’s Special Offer: {offer}")
        print("\n Bill generated on:", datetime.datetime.now().strftime("%d-%b-%Y %H:%M:%S"))
>>>>>>> phase-2

# Program Flow (Conditionals + Functions)
show_menu()
while True:
    take_order()
    more = input("Add more items? (y/n): ")
    if more.lower() != 'y':
        break

<<<<<<< HEAD
# Generate Bill with Exception Handling
=======
#  Generate Bill with Exception Handling
>>>>>>> phase-2
try:
    discount = int(input("\nEnter discount percentage (0 if none): "))
    if discount < 0:
        raise ValueError("Discount cannot be negative!")
except ValueError as e:
    print(f" Invalid discount: {e}")
    discount = 0

# Generate and display final bill
bill = DiscountedBill(orders, discount)
bill.generate_bill()
print("\n Thank you for visiting CaterLeap Café!")
