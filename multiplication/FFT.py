import numpy as np


def horner(poly, x):
    # poly = (a0, a1, ..., an-1)
    result = poly[-1]
    for i in range(len(poly) - 2, -1, -1):
        result = result * x + poly[i]
    return int(result)


def FFT_multiplication(a, b):
    # for any two polynomials a and b
    # a = (a0, a1, ..., an-1)
    # b = (b0, b1, ..., bm-1)

    na = len(a)
    nb = len(b)

    # n is a power of 2
    n = int(2 ** np.ceil(np.log2(na + nb - 1)))

    # # padding
    a = np.pad(a, (0, n - na))
    b = np.pad(b, (0, n - nb))

    # # a conv b = DFT^-1(DFT(a) * DFT(b))
    fft_a = DFT(a)
    fft_b = DFT(b)
    fft_c = fft_a * fft_b
    c = DFT(fft_c, inverse=True)
    return c


def FFT_integer_multiplication(a, b):
    # a and b are integers
    # represent a and b as polynomials
    # a = (a0, a1, ..., an-1)
    # b = (b0, b1, ..., bm-1)
    a = np.array([int(i) for i in str(a)])[::-1]
    b = np.array([int(i) for i in str(b)])[::-1]
    c = FFT_multiplication(a, b)
    # result = int(sum([c[i] * 10**i for i in range(len(c))]))
    result = horner(c, 10)
    return result


def DFT(a, inverse=False):
    y = FFT(a, inverse)
    if not inverse:
        return y
    else:
        n = len(a)
        return np.round(y.real / n, n)


# evaluation of point-value pairs
def FFT(a, inverse=False):
    # the length of a must be a power of 2
    n = len(a)
    if n == 1:
        return a
    else:
        if not inverse:
            phase = -2j * np.pi / n
        else:
            phase = 2j * np.pi / n
        wn = np.exp(phase)
        w = 1

        # divide and conquer
        a_0 = a[::2]
        a_1 = a[1::2]
        y_0 = FFT(a_0, inverse)
        y_1 = FFT(a_1, inverse)

        y = np.zeros(n, dtype=complex)
        for k in range(int(n / 2)):
            # A(x) = Aeven(x^2) + x * Aodd(x^2)
            # A(-x) = Aeven(x^2) - x * Aodd(x^2) -> -xi = x(i+n/2)
            # x = wn^i -> wn^(i+n/2) = -wn^i
            y[k] = y_0[k] + w * y_1[k]
            y[k + int(n / 2)] = y_0[k] - w * y_1[k]
            w = w * wn
        return y


# ex1
# x = np.array([1, 0, 0, 1])
# y = np.array([2, 1 + 1j, 0, 1 - 1j])

# print(DFT(x))
# print(DFT(y, inverse=True))

# ex2
# x = np.array([1, 2, 0, 3, 0, 1, 3, 2])
# y = DFT(x)
# print(y)
# print(DFT(y, inverse=True))

# ex3
# x = np.array([1 ,2, 0, 3])
# y = DFT(x)
# print(y)
# print(DFT(y, inverse=True))

# ex4(polynomial multiplication)
# a = np.array([2, -2, 1])
# b = np.array([2, 2, 1])
# # result [ 4.  0.  0.  0.  1.  0. -0.  0.]
# print(FFT_multiplication(a, b))

# ex5 (polynomial multiplication: book example)
# a = np.array([9, -10, 7, 6])
# b = np.array([-5, 4, 0, -2])
# # result [-45.  86. -75. -20.  44. -14. -12.  -0.]
# print(FFT_multiplication(a, b))

# ex6(integer multiplication)
# a = 14
# b = 37
# print(FFT_integer_multiplication(a, b))

# test
a = [3, 1]
b = [5, 2]
print(FFT_multiplication(a, b))
