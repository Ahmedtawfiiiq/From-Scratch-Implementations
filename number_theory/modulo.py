from math import gcd, factorial

def modulo(a, n):
    return a % n

a = factorial(4) # 4! = 4 * 3 * 2 * 1 = 24
n = 3
print(modulo(a, n))
# print(gcd(a, n))
