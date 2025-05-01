#Python program to create a 1D, 2D, 
#and 3D NumPy array. Perform basic operations like reshaping, slicing, and indexing.

import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
c = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# reshaping
shape_a = a.reshape(5, 1)
shape_b = b.reshape(3, 3)
shape_c = c.reshape(2, 2, 2)

# slicing
slice_a = a[1:4]
slice_b = b[1:3, 1:3]
slice_c = c[0:2, 0:2, 0:2]

# indexing
index_a = a[4]
index_b = b[2, 2]
index_c = c[1, 1, 1]
