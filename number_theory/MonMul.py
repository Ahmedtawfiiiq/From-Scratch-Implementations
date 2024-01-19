def gcd_extended(a, b):
    # a and b are any integers, not both zero
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = gcd_extended(b, a % b)
        return d, y, x - y * (a // b)


def gcd_extended_inverse(a, b):
    d, x, _ = gcd_extended(a, b)
    if d == 1:
        return x % b
    else:
        return None


def gcd_recursion(a, b):
    # a is any non-negative integer: 0, 1, 2, 3, ...
    # b is any positive integer: 1, 2, 3, ...
    if b == 0:
        return a
    else:
        return gcd_recursion(b, a % b)


# montgomery multiplication
def MonPro(a_bar, b_bar, n, r):
    t = (a_bar * b_bar) % r
    # n*n^-1 + r*r^-1 = 1
    # n' = -n^-1 mod r
    n_inv = gcd_extended_inverse(n, r)
    n_dash = n_inv * (-1)
    m = (t * n_dash) % r
    u = (a_bar * b_bar + m * n) // r
    if u >= n:
        return u - n
    else:
        return u


def MonMul(a, b, n):
    # n is odd
    # a, b, n are k bits
    # r = 2^k
    k = len(bin(n)[2:])  # [2:] to remove '0b' from the string
    r = 2**k
    if gcd_recursion(r, n)!= 1:
        raise ValueError("r and n are not coprime")
    a_bar = (a * r) % n
    b_bar = (b * r) % n
    x_bar = MonPro(a_bar, b_bar, n, r)
    x = MonPro(x_bar, 1, n, r)
    return x


a = 7**3
b = 7**2
n = 19
x = MonMul(a, b, n)
print("{0} * {1} mod {2} = {3}".format(a, b, n, x))
print((a * b) % n)
