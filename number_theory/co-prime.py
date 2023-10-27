from math import gcd

def is_coprime(l):
    g = l[0]
    for ele in l[1:]:
        g = gcd(g, ele)
    return g == 1


arr = [3, 3, 2]
print(is_coprime(arr))
