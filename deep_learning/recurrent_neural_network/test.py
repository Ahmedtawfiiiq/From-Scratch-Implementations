import numpy as np

# A is a 3x3 matrix
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# B is a 3x1 matrix
B = np.array([[1], [2], [3]])

print(A @ B)
print(B @ A.T)
