import numpy as np


def horner(poly, x):
    result = poly[0]
    for i in range(1, len(poly)):
        result = result * x + poly[i]
    return result

    
def karatsuba(x, y, integer=True):
    if integer:
        x = [int(i) for i in str(x)]
        y = [int(i) for i in str(y)]
    if len(x) != len(y):
        n = int(2 ** np.ceil(np.log2(len(x) + len(y) - 1)))
        x = np.pad(x, (n - len(x), 0))
        y = np.pad(y, (n - len(y), 0))
    coefficients = karatsuba_multiplication(x, y)
    if integer:
        return horner(coefficients, 10)
    else:
        return coefficients


def karatsuba_multiplication(x, y):
    n = len(x)

    if n == 1:
        return [x[0] * y[0]]

    split = n // 2

    # x = x1 * 10^(n//2) + x0
    x0 = x[:split]
    x1 = x[split:]

    # y = y1 * 10^(n//2) + y0
    y0 = y[:split]
    y1 = y[split:]

    m0 = karatsuba_multiplication(x0, y0)
    m1 = karatsuba_multiplication(x1, y1)

    x = [(x0[i] + x1[i]) for i in range(split)]
    y = [(y0[i] + y1[i]) for i in range(split)]

    m2 = karatsuba_multiplication(x, y)
    m2 = [(m2[i] - m0[i] - m1[i]) for i in range(len(m2))]

    coefficients = [0] * (n * 2 - 1)
    for i in range(len(m0)):
        coefficients[i] += m0[i]
        coefficients[i + split] += m2[i]
        coefficients[i + n] += m1[i]
    return coefficients


x = 12344
y = 4321
print(karatsuba(x, y))

a = [6, 7, -10, 9]
b = [-2, 0, 4, -5]
print(karatsuba(a, b, integer=False))
