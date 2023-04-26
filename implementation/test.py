import numpy as np


def max_positive_difference(prices):
    return max(
        [
            prices[i] - prices[j]
            for i in range(1, len(prices))
            for j in range(i)
            if prices[i] > prices[j]
        ]
    )


array = np.random.rand(1000000)
print(max_positive_difference(array))
