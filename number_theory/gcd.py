# using Euclid's algorithm
def gcd_recursion(a, b):
    # a is any non-negative integer: 0, 1, 2, 3, ...
    # b is any positive integer: 1, 2, 3, ...
    if b == 0:
        return a
    else:
        return gcd_recursion(b, a % b)


# using extended Euclid's algorithm
def gcd_extended(a, b):
    # a and b are any integers, not both zero
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = gcd_extended(b, a % b)
        return d, y, x - y * (a // b)


def gcd_extended_inverse(a, b):
    d, x, y = gcd_extended(a, b)
    if d == 1:
        return x % b
    else:
        return None


a = 3
b = 1
gcd = gcd_recursion(a, b)
print("gcd recursive({0}, {1}) = {2}".format(a, b, gcd))
# gcd = gcd_extended(a, b)
# print("gcd extended ({0}, {1}) = {2}".format(a, b, gcd[0]))
# print("{0}(a) * {1}(x) + {2}(b) * {3}(y) = {4}(gcd)".format(a, gcd[1], b, gcd[2], gcd[0]))
# format in the form of x = gcd[1], y = gcd[2], gcd = gcd[0]
# print("gcd is {0}, (a, x) is ({1}, {2}), (b, y) is ({3}, {4})".format(gcd[0], a, gcd[1], b, gcd[2]))
# gcd = gcd_extended_inverse(a, b)
# print("gcd extended inverse ({0}, {1}) = {2}".format(a, b, gcd))
