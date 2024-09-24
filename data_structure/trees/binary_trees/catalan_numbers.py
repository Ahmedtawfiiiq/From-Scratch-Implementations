def catalan_numbers(n):
    if n == 0:
        return 1
    else:
        return ((4 * n) - 2) * catalan_numbers(n - 1) // (n + 1)


print(catalan_numbers(19))
