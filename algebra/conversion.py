def toInt(c):
    letters = "0123456789ABCDEF"
    return letters.find(c)  # return index of given character c


def to_decimal(s, base):
    result = 0
    for i in range(len(s)):
        # horner's algorithm
        result = result * base + toInt(s[i])
    return result


def from_decimal(n, base):
    letters = "0123456789ABCDEF"
    if n == 0:
        return "0"
    result = ""
    while n != 0:
        result = letters[n % base] + result
        n //= base
    return result


a = 193
h = from_decimal(a, 2)
print(h)
print(to_decimal(h, 2))
