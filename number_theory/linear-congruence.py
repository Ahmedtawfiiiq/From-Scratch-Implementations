from gcd import gcd_recursion, gcd_extended_inverse


# check if ax congruent to b (mod n) is solvable
def is_solvable(a, b, n):
    d = gcd_recursion(a, n)
    if b % d == 0:
        return d
    else:
        return None


def linear_congruence(a, b, n):
    d = is_solvable(a, b, n)
    if d is None:
        return None
    else:
        sep = n // d
        a //= d
        b //= d
        n //= d
        a_inv = gcd_extended_inverse(a, n)
        x = (a_inv * b) % n
        solutions = []
        for i in range(d):
            solutions.append(x + (i * sep))
        return solutions

a = 1
b = -1
n = 4
solutions = linear_congruence(a, b, n)
print("solutions of {0}x congruent to {1} (mod {2})".format(a, b, n))
print(solutions)
