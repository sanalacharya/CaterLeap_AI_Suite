#*******NUMPY BASICS******

import numpy as np

# 1D and 2D Arrays
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

print("Array 1:", arr1)
print("Array 2:\n", arr2)

# Array Operations
print("Sum:", np.sum(arr1))
print("Mean:", np.mean(arr2))
print("Shape:", arr2.shape)
print("Reshape:\n", arr2.reshape(3, 2))

#Array Attributes
a = np.array([[1, 2, 3], [4, 5, 6]])

print("Shape:", a.shape)
print("Dimensions:", a.ndim)
print("Data Type:", a.dtype)
print("Size:", a.size)


#Array Operation
x = np.array([10, 20, 30])
y = np.array([1, 2, 3])

print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Square root:", np.sqrt(x))
print("Exponential:", np.exp(y))
print("Dot product:", np.dot(x, y))

#Stastical Operation
x = np.array([10, 20, 30])
y = np.array([1, 2, 3])

print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Square root:", np.sqrt(x))
print("Exponential:", np.exp(y))
print("Dot product:", np.dot(x, y))
