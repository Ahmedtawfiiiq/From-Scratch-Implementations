def t(n):
    if n == 1:
        return 1
    return 3 * t(n / 2) + n**2


print(t(8))
