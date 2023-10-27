import numpy as np


def group_generator(group, generator, divisor):
    if len(group) == 0:
        print("Group is empty")
        return None
    if generator not in group:
        print(f"Generator {generator} not in group {group}")
        return None
    elements = np.array([])
    i = 1
    while i <= len(group):
        # multiplication modulo divisor
        elements = np.append(elements, ((generator**i) % divisor))
        i += 1
    return elements


group = np.array([1, 3, 4, 5, 9])
generator = 3
divisor = 11
print(modulo(group, generator, divisor))
