def modExp(a, b, n):
    d = 1
    while b > 0:
        if b & 1 == 1:
            d = (d * a) % n
        b >>= 1
        a = (a * a) % n
    return d


a = 7
b = 13
n = 11
print(modExp(a, b, n))
