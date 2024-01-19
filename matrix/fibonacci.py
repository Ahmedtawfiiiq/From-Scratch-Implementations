import numpy as np


def multiplication(m1, m2):
    rows = len(m1)
    cols = len(m2[0])
    result = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            for k in range(len(m2)):
                result[i][j] += m1[i][k] * m2[k][j]
    return result


def power(matrix, n):
    if n == 0:
        return np.eye(len(matrix))

    if n % 2 == 0:
        return power(multiplication(matrix, matrix), n // 2)
    else:
        return multiplication(matrix, power(matrix, n - 1))


def power_block(matrix, n):
    l = len(matrix)
    nn = np.zeros((2 * l, 2 * l))
    for i in range(l):
        for j in range(l):
            nn[i][j] = matrix[i][j]
            nn[i + l][j] = matrix[i][j]
            nn[i + l][j + l] = 1 if i == j else 0
    return power(nn, n)[0:l, 0:l]


def fibonacci(n):
    # transition matrix
    t = np.array([[0, 1], [1, 1]])
    # initial vector
    v = np.array([[0], [1]])
    # return the n-th fibonacci number
    f = multiplication(power(t, n - 1), v)
    return int(f[1][0])


# print(fibonacci(10))
m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(power_block(m, 2))
print(power(m, 2))
