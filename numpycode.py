import numpy as np


array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", array_1d)

# Create a 2D array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", array_2d)

# Perform basic arithmetic operations
array_sum = array_1d + 10
print("Array after adding 10:", array_sum)

array_product = array_1d * 2
print("Array after multiplying by 2:", array_product)

# Calculate mean and standard deviation
mean = np.mean(array_1d)
std_dev = np.std(array_1d)
print("Mean:", mean)
print("Standard Deviation:", std_dev)

# Matrix multiplication
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])
matrix_product = np.dot(matrix_a, matrix_b)
print("Matrix Product:\n", matrix_product)
