import numpy as np
from colorama import Fore, Style


def modular_table(group, modulus, operation):
    table = np.array([])
    for ele in group:
        row = np.array([])
        for ele2 in group:
            if operation == "+":
                result = (ele + ele2) % modulus
            elif operation == "*":
                result = (ele * ele2) % modulus
            row = np.append(row, result)
        table = np.append(table, row)
    return table.reshape(len(group), len(group))


# n = 5
# group = np.array([0, 1, 2, 3, 4, 5, 6, 7])
# group = np.array([1, 3, 4, 5, 9])
# group = np.array(list(range(0, n)))
# modulus = n

modulus = 15
group = np.array([1, 2, 4, 7, 8, 11, 13, 14])

print("Addition table:")
table = modular_table(group, modulus, "+")
print(table)
print("Multiplication table:")
table = modular_table(group, modulus, "*")
print(table)
