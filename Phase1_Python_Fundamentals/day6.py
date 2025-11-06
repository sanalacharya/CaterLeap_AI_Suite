#default parameter
<<<<<<< HEAD

=======
>>>>>>> phase-2
def bill_amount(amount, tax=0.05):
    return amount + (amount * tax)

print("Bill Total:", bill_amount(1000))        # Default 5% tax
print("Bill Total:", bill_amount(1000, 0.18))  # Custom 18% tax

<<<<<<< HEAD
=======

>>>>>>> phase-2
discount = 10  # Global variable

def apply_discount(price):
    discount = 5  # Local variable
    return price - (price * discount / 100)

print("Discounted Price:", apply_discount(500))
print("Global Discount Value:", discount)


<<<<<<< HEAD
#mini project
=======
#Mini Project: Catering Bill Calculator

>>>>>>> phase-2
def calculate_total(prices):
    total = 0
    for price in prices:
        total += price
    return total

items = [150, 200, 300, 100]
print("Items:", items)
print("Total Bill Amount: ₹", calculate_total(items))
<<<<<<< HEAD
=======


>>>>>>> phase-2
