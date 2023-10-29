def divisors(n):
    if n < 1:
        raise ValueError("n must be positive")
    divs = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            divs.append(i)
            if i * i != n:
                divs.append(n // i)
        i += 1

    return sorted(divs)

from math import factorial

n = 24**3
print(len(divisors(n)))
