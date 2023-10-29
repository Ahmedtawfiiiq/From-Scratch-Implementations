from prime import prime_factorization
def euler_totient(n):
    # phi function is the number of positive
    # integers less than n which are coprime to n
    # phi(n) = n * prod(1 - 1/p) for all prime p
    # for p in prime_factorization(n):
    #     n *= 1 - 1 / p
    for p in prime_factorization(n):
        n //= p
        n *= p - 1
    return n



n = 10
print(euler_totient(n))
