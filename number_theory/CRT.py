from functools import reduce
from gcd import gcd_extended_inverse


def chinese(residues, moduli):
    k = len(residues)
    # M = m1*m2*...*mk
    M = reduce(lambda x, y: x * y, moduli)
    # Mi = M/mi
    Mi = [M // mi for mi in moduli]
    # Mi_inverse = Mi^-1 mod mi
    Mi_inverse = [gcd_extended_inverse(Mi[i], moduli[i]) for i in range(k)]
    ci = [Mi[i] * (Mi_inverse[i] % moduli[i]) for i in range(k)]
    # A = (a1*c1 + a2*c2 + ... + ak*ck) mod M
    A = reduce(lambda x, y: x + y, [residues[i] * ci[i] for i in range(k)]) % M
    return A


def chinese_operations(A, B, moduli, operation):
    k = len(moduli)
    a = [A % mi for mi in moduli]
    b = [B % mi for mi in moduli]
    if operation == "+":
        c = [(a[i] + b[i]) for i in range(k)]
    elif operation == "-":
        c = [(a[i] - b[i]) for i in range(k)]
    elif operation == "*":
        c = [(a[i] * b[i]) for i in range(k)]
    return chinese(c, moduli)


# ex0 (lecture example)
# residues = [2, 3]
# moduli = [5, 13]
# A = chinese(residues, moduli)
# print("A = {0}".format(A)) # A = 42

# ex1
# residues = [3, 1, 6]
# moduli = [5, 7, 8]
# A = chinese(residues, moduli)
# print("A = {0}".format(A)) # A = 78

# ex2
# residues = [12, 6]  # a1, a2, ..., ak
# moduli = [37, 49]  # m1, m2, ..., mk
# A = chinese(residues, moduli)
# print("A = {0}".format(A))  # A = 937

# ex3
# A = 973
# B = 678
# moduli = [37, 49]
# # perform C = A + B
# C = chinese_operations(A, B, moduli, "+")
# print("C = {0}".format(C)) # C = 1651

# ex4
# A = 1651
# B = 73
# moduli = [37, 49]
# # perform C = A * B
# C = chinese_operations(A, B, moduli, "*")
# print("C = {0}".format(C)) # C = 865


residues = [4, 3]
moduli = [7, 6]
A = chinese(residues, moduli)
print("A = {0}".format(A)) # A = 42
