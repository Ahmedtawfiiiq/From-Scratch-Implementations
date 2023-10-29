def is_prime(n):
    if n == 2:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def prime_factorization(n):
    if n <= 1:
        return []
    i = 2
    factorization = []
    while i * i <= n:
        if n % i == 0:
            factorization.append(i)
            while n % i == 0:
                n //= i
        else:
            i += 1
    if n > 1:  # n is prime
        factorization.append(n)
    return factorization


# sieve of eratosthenes (problem solving)
def count_primes(n):
    if n <= 2:
        return 0
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    i = 2
    while i * i <= n:
        if primes[i]:
            j = i * i
            while j <= n:
                primes[j] = False
                j += i
        i += 1
    return sum(primes)


# x = 10
# c = count_primes(x)
# print(c)

from math import factorial

n = 10
# print(prime_factorization(factorial(n)))
