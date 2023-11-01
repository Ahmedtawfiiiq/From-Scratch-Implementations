import numpy as np


def DFT(a, inverse=False):
    N = len(a)
    if not inverse:
        phase = -2j * np.pi / N
    else:
        phase = 2j * np.pi / N
    y = np.zeros(N, dtype=complex)
    w = np.array([np.exp(phase * k) for k in range(N)])
    for k in range(N):
        for n in range(N):
            y[k] += a[n] * w[(k * n) % N]
    if inverse:
        y /= N
        return np.round(y.real, 5)
    return y


x = np.array([1, 2, 0, 3, 0, 1, 3, 2])
y = DFT(x)
print(y)
print(DFT(y, inverse=True))
