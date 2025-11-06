
# Inheritance

#Inheritance
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
#Using super() and Constructor Inheritance
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

#Method Overridinig
# Example
car1 = Car("Tesla", 4, "Electric")
car1.show_details()

#Method Overriding
class Employee:
    def work(self):
        print("Employee works 8 hours a day.")

class Developer(Employee):
    def work(self):
        print("Developer writes code 10 hours a day.")
# Example
emp = Employee()
dev = Developer()

emp.work()   # Parent method
dev.work()   # Overridden method


#Multilevel Inheritance
class GrandParent:
    def greet(self):
        print("Hello from GrandParent!")

class Parent(GrandParent):
    def show(self):
        print("Hello from Parent!")

class Child(Parent):
    def display(self):
        print("Hello from Child!")

child = Child()
child.greet()
child.show()
child.display()
