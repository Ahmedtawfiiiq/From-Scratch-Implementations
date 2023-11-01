import numpy as np


def DFT(a, inverse=False):
    y = FFT(a, inverse)
    if not inverse:
        return y
    else:
        y /= len(a)
        return y.real


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

        a_0 = a[::2]
        a_1 = a[1::2]

        y_0 = FFT(a_0, inverse)
        y_1 = FFT(a_1, inverse)

        y = np.zeros(n, dtype=complex)
        for k in range(int(n / 2)):
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
a = np.array([5, 3])
b = np.array([2])
n = len(a) + len(b) - 1

# # padding
a = np.pad(a, (0, n - len(a)))
b = np.pad(b, (0, n - len(b)))

# # a conv b = DFT^-1(DFT(a) * DFT(b))
fft_a = DFT(a)
fft_b = DFT(b)
fft_c = fft_a * fft_b
c = DFT(fft_c, inverse=True)
print(c)
