# 1D dynamic programming
def rod_cutting(p, n):
    if n == 0:
        return 0
    q = -1
    for i in range(1, n + 1):
        q = max(q, p[i] + rod_cutting(p, n - i))
    return q


def bottom_up_rod_cutting(p, n):
    r = [0] * (n + 1)
    for j in range(1, n + 1):
        q = -1
        for i in range(1, j + 1):
            if p[i] + r[j - i] > q:
                q = p[i] + r[j - i]
        r[j] = q
    return r


def extended_bottom_up_rod_cutting(p, n):
    r = [0] * (n + 1)
    s = [0] * (n + 1)
    for j in range(1, n + 1):
        q = -1
        for i in range(1, j + 1):
            if p[i] + r[j - i] > q:
                q = p[i] + r[j - i]
                s[j] = i  # the length of the first piece to cut off
        r[j] = q
    # reconstruct the cuts
    cut = []
    while n > 0:
        cut.append(s[n])
        n -= s[n]
    return r, s, cut


def modified_rod_cutting(p, c, n):
    r = [0 for _ in range(n + 1)]
    for j in range(1, n + 1):
        q = p[j]
        for i in range(1, j):
            q = max(q, p[i] + r[j - i] - c)
        r[j] = q
    return r[-1]


p = [0, 1, 5, 8, 9, 10, 17, 17, 20]
fixed_cost = 3
# print(rod_cutting(p, 4))
print(bottom_up_rod_cutting(p, 8))
# print(extended_bottom_up_rod_cutting(p, 8))
print(modified_rod_cutting(p, fixed_cost, 8))
