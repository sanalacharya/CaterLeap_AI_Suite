# Define a simple class
class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Course: {self.course}")

# Create an object
student1 = Student("Jithu Viji", "Artificial Intelligence and Data Science")
student1.show_details()

#multiple steps in class

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def multiply(self):
        return self.a * self.b

# Create object and call methods
calc = Calculator(10, 5)
print("Addition:", calc.add())
print("Multiplication:", calc.multiply())


# restaurant billing system
class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = {"Paneer Butter Masala": 180, "Veg Biryani": 150, "Gobi Manchurian": 130}
        self.bill = 0

    def show_menu(self):
        print(f"Welcome to {self.name}!")
        for item, price in self.menu.items():
            print(f"{item}: ₹{price}")

    def order_item(self, item_name, quantity):
        if item_name in self.menu:
            total = self.menu[item_name] * quantity
            self.bill += total
            print(f"Added {quantity} x {item_name} = ₹{total}")
        else:
            print("Item not available!")

    def final_bill(self):
        print(f"\nTotal Bill Amount: ₹{self.bill}")

# Example
r = Restaurant("CaterLeap Café")
r.show_menu()
r.order_item("Paneer Butter Masala", 2)
r.order_item("Veg Biryani", 1)
r.final_bill()

