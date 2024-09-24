# annihilation operator matrix using kronecker delta
import numpy as np

n = 4

creation = lambda i, j: np.sqrt(i) if i == j + 1 else 0
a_dagger = np.array([[creation(i, j) for j in range(n)] for i in range(n)])
# print(a_dagger)

annihilation = lambda i, j: np.sqrt(i + 1) if i + 1 == j else 0
a = np.array([[annihilation(i, j) for j in range(n)] for i in range(n)])
print(a)
