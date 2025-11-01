# Inheritance
# Parent Class
class Animal:
    def speak(self):
        print("Animals make different sounds.")

# Child Class
class Dog(Animal):
    def bark(self):
        print("Dog says Woof!")

# Object creation
dog = Dog()
dog.speak()   # inherited method
dog.bark()    # child class method


#Constroctor inheritance
class Vehicle:
    def __init__(self, brand, wheels):
        self.brand = brand
        self.wheels = wheels

    def display(self):
        print(f"Brand: {self.brand}, Wheels: {self.wheels}")

class Car(Vehicle):
    def __init__(self, brand, wheels, fuel_type):
        super().__init__(brand, wheels)
        self.fuel_type = fuel_type

    def show_details(self):
        self.display()
        print(f"Fuel Type: {self.fuel_type}")

# Example
car1 = Car("Tesla", 4, "Electric")
car1.show_details()
