import numpy as np
from torch.nn import Softmax
from torch import tensor


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


y = [0.64, 0, 0, 0.0716] # estimated output
t = tensor([0.64, 0, 0, 0.0716]) # tensor version

print(softmax(y))
print(deriv_softmax(y))

s = Softmax(dim=0)
# s = torch.softmax(dim=0) # deprecated
print(s(t))
