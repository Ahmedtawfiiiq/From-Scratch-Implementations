import numpy as np


def polynomial_convolution(a, b):
    # perform polynomial multiplication using convolution
    # a = (a0, a1, ..., an-1)
    # b = (b0, b1, ..., bn-1)
    na = len(a)
    nb = len(b)
    nc = na + nb - 1
    # pad a and b with zeros to make them of same length of nc
    a = np.pad(a, (0, nc - na))
    b = np.pad(b, (0, nc - nb))
    # perform convolution
    j = 0
    k = 0
    c = np.zeros(nc)
    while j < nc:
        while k <= j:
            c[j] += a[k] * b[j - k]
            k += 1
        j += 1
        k = 0
    return c


a_coef = [9, -10, 7, 6]
b_coef = [-5, 4, 0, -2]
print(polynomial_convolution(a_coef, b_coef))
