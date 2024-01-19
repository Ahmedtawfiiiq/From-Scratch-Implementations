def power(a, b):
    if b == 0:
        return 1
    if b % 2 == 0:
        return power(a * a, b // 2)
    else:
        return a * power(a * a, b // 2)


a = 2
b = 10
print("{0}^{1} = {2}".format(a, b, power(a, b)))
