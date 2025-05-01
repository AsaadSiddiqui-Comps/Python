#Write a Python program to calculate mean, median, standard deviation, variance, and correlation coefficients of a given array

import numpy as np

A = np.array([10, 20, 30, 40, 50])
B = np.array([5, 25, 35, 45, 60])

mean_val = np.mean(A)
print("Mean:", mean_val)

median_val = np.median(A)
print("Median:", median_val)

std_dev = np.std(A)
print("Standard Deviation:", std_dev)

variance_val = np.var(A)
print("Variance:", variance_val)

correlation_matrix = np.corrcoef(A, B)
print("Correlation Coefficient Matrix:\n", correlation_matrix)

