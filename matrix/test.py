import numpy as np
from fibonacci import power, multiplication


def fun(round):
    v = np.array([[1], [0], [4]])
    transition_matrix = np.array([[0, 1, 1], [1, 0, 1], [1, 1, 0]])
    return multiplication(power(transition_matrix, round), v)


print(fun(4))
