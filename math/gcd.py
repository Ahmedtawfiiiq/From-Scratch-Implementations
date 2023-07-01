def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def gcd2(a, b):
    s = min(a, b)
    for i in range(s, 0, -1):  # s is included and 0 is excluded with step -1
        if a % i == 0 and b % i == 0:
            return i


a = 60
b = 48

print(gcd(a, b))
print(gcd2(a, b))
