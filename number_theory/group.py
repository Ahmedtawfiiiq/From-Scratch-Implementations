import numpy as np


def group_generator(group, generator, divisor, type="additive"):
    if len(group) == 0:
        print("Group is empty")
        return None
    if generator not in group:
        print(f"Generator {generator} not in group {group}")
        return None
    elements = np.array([])
    i = 1
    while i <= len(group):
        if type == "additive":
            elements = np.append(elements, (generator*i) % divisor)
        elif type == "multiplicative":
            elements = np.append(elements, ((generator**i) % divisor))
        i += 1
    for g in group:
        if g not in elements:
            print(f"{generator} is not a generator")
            return
    print(f"{generator} is a generator")
    print(f"Elements: {elements}")
    return


n = 11
group = np.array(list(range(1, n)))
divisor = n
for g in group:
    group_generator(group, g, divisor, type="multiplicative")
