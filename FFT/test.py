import numpy as np


def rev(k, n):
    result = 0
    n_bits = 2
    while n_bits > 0:
        result <<= 1
        result ^= k & 1
        k >>= 1
        n_bits -= 1
    return result


def BIT_REVERSE_COPY(a):
    n = len(a)
    A = np.zeros(n)
    for k in range(n):
        A[rev(k, n)] = a[k]
    return A


def ITERATIVE_FFT(a):
    A = BIT_REVERSE_COPY(a)
    n = len(a)  # n is a power of 2
    for s in range(1, int(np.log2(n)) + 1):
        m = 2**s
        wm = np.exp(-2j * np.pi / m)
        for k in range(0, n, m):
            w = 1
            for j in range(0, m // 2):
                t = w * A[k + j + m // 2]
                u = A[k + j]
                # add two complex numbers u and t
                A[k + j] = u + t
                # subtract two complex numbers u and t
                # without discarding imaginary part
                A[k + j + m // 2] = u - t
                w *= wm
    return A


def twiddle_factors(N):
    w = np.exp(-2j * np.pi * np.arange(N) / N)
    return np.round(w, N)


# a = np.array([0, 4, 2, 6, 1, 5, 3, 7])
# print(ITERATIVE_FFT(a))
# print(twiddle_factors(4))
