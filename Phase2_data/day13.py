#numpy Basics
import numpy as np

# Create arrays with zeros, ones, and random numbers
zeros_arr = np.zeros((2, 3))
ones_arr = np.ones((3, 2))
rand_arr = np.random.rand(2, 3)   # random numbers between 0 and 1

print("Zeros Array:\n", zeros_arr)
print("\nOnes Array:\n", ones_arr)
print("\nRandom Array:\n", rand_arr)

# Create a sequence of numbers
seq_arr = np.arange(10, 50, 5)
print("\nSequence Array:", seq_arr)

# Evenly spaced numbers
lin_arr = np.linspace(0, 1, 5)
print("\nLinearly spaced:", lin_arr)

#*************************
#Array Attributes
#*************************

a = np.array([[1, 2, 3], [4, 5, 6]])

print("Shape:", a.shape)
print("Dimensions:", a.ndim)
print("Data Type:", a.dtype)
print("Size:", a.size)


#Array Operations
x = np.array([10, 20, 30])
y = np.array([1, 2, 3])

print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Square root:", np.sqrt(x))
print("Exponential:", np.exp(y))
print("Dot product:", np.dot(x, y))

#Stastical operation
arr = np.array([10, 20, 30, 40, 50])

print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))
print("Min:", np.min(arr))
print("Max:", np.max(arr))
