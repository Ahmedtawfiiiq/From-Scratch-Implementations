# 1D dynamic programming
def recursive_rodCutting(p, n):
    if n == 0:
        return 0
    q = -1
    for i in range(1, n + 1):
        q = max(q, p[i] + recursive_rodCutting(p, n - i))
    return q


def solve(p, n):
    p = [0] + p
    return recursive_rodCutting(p, n)


p = [1, 5, 8, 9, 10, 17, 17, 20]
print(solve(p, 8))
