# Develop a Python script to create two arrays of the same shape and perform element-wise addition, subtraction, multiplication, and division. Calculate the dot product and cross product of two vectors
import numpy as np

A = np.array([2, 4, 6])
B = np.array([1, 3, 5])

print("Array 1:", A)
print("Array 2:", B)

print("Addition:", A + B)
print("Subtraction:", A - B)
print("Multiplication:", A * B)
print("Division:", A / B)

dot_product = np.dot(A, B)
print("Dot Product:", dot_product)
cross_product = np.cross(A, B)
print("Cross Product:", cross_product)
