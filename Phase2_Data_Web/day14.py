#Matrix operation
import numpy as np
x = np.array([10, 20, 30])
y = np.array([1, 2, 3])

print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Square root:", np.sqrt(x))
print("Exponential:", np.exp(y))
print("Dot product:", np.dot(x, y))


#Indexing, Slicing, and Boolean Filtering
arr = np.array([10, 20, 30, 40, 50])

print("First 3 elements:", arr[:3])
print("Last 2 elements:", arr[-2:])
print("Values > 25:", arr[arr > 25])

# 2D Example
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\nSecond row:", matrix[1])
print("Element (3rd row, 2nd col):", matrix[2, 1])

#Reshaping and Combining Arrays
arr = np.arange(1, 13)

print("Original Array:", arr)
reshaped = arr.reshape(3, 4)
print("\nReshaped (3x4):\n", reshaped)

# Stacking arrays
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print("\nVertical Stack:\n", np.vstack((a, b)))
print("\nHorizontal Stack:\n", np.hstack((a, b)))

#Real Example – Restaurant Sales Analysis
import numpy as np

# Sales data for 5 days (3 items)
sales = np.array([
    [1200, 800, 950],   # Day 1
    [1100, 850, 1000],  # Day 2
    [1300, 900, 1050],  # Day 3
    [1250, 950, 1100],  # Day 4
    [1400, 1000, 1200]  # Day 5
])

# Total and average sales
total_per_item = np.sum(sales, axis=0)
average_sales = np.mean(sales, axis=0)

print("Total sales per item:", total_per_item)
print("Average sales per item:", average_sales)
print("Overall total:", np.sum(sales))

