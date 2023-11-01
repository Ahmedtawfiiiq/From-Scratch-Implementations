def horner(poly, x):
    result = poly[0]
    for i in range(1, len(poly)):
        result = result * x + poly[i]
    return result


polynomial = [2, 3, -4, 1]
x = 8
print(horner(polynomial, x))
