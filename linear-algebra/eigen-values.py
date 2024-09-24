import numpy as np

A = np.array([[1, 6], [5, 2]])

U = np.array([[1, -2], [2, 1]]) / np.sqrt(5)
D = np.sqrt(10) * np.array([[2, 0], [0, 1]])

print(U @ D / np.sqrt(2))
Inv = np.linalg.inv(U @ D)
print(Inv)
