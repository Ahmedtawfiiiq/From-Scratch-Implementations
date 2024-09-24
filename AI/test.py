# x-z decomposition of unitary gates

import numpy as np

U = np.sqrt(1 / 2) * np.array(
    [
        [1, -1j],
        [-1j, 1],
    ]
)

# x-z decomposition
a = np.sqrt(1 / 2) * np.array([[1, -1j], [-1j, 1]])

b = np.linalg.inv(a) @ U @ np.linalg.inv(a)

print(a * np.sqrt(2))
