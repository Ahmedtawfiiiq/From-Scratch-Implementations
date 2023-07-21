import numpy as np


# description
# softmax function is used to convert the output into a probability distribution
# used in the output layer of the neural network for multi-class classification problems
def softmax(x):
    e_x = np.exp(x)
    return e_x / sum(e_x)


def deriv_softmax(x):
    l = len(x)
    grad = np.zeros((l, l))
    # grad is a symmetric matrix
    for i in range(l):
        grad[i, i] = x[i] * (1 - x[i])
        for j in range(i + 1, l):
            grad[i, j] = -x[i] * x[j]
            grad[j, i] = grad[i, j]
    return grad


y = [1.1, 2.2, 0.2, -1.7]
s = softmax(y)
# round to 3 decimal places
s = np.round(s, 3)
# print(s)
g = deriv_softmax(s)
# print(g)
