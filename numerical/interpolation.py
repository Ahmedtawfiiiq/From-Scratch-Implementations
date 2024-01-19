import numpy as np


def horner(poly, x):
    result = poly[0]
    for i in range(1, len(poly)):
        result = result * x + poly[i]
    return result


def lagrange_interpolation(x, y, x0):
    # given point-value pairs
    # return the value of the interpolating polynomial at x0
    n = len(x)
    y0 = 0
    for i in range(n):
        p = 1
        for j in range(n):
            if i != j:
                p *= (x0 - x[j]) / (x[i] - x[j])
        y0 += p * y[i]
    return y0


def vandermode(x, y):
    v = np.zeros((len(x), len(x)))
    v[:, 0] = 1
    for i in range(1, len(x)):
        v[:, i] = v[:, i - 1] * x
    # given point-value pairs
    # return coefficients of the polynomial
    # a = (a0, a1, ..., an-1)
    return np.round(np.linalg.solve(v, y), 2)


x = np.array([-1, 0, 1])
y = np.array([horner([3, -1, 2], ele) for ele in x])
# print(lagrange_interpolation(x, y, 2))
print(vandermode(x, y))
