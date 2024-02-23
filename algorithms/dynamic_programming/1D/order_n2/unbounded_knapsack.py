def fun(w, v, n):
    if n == 0:
        return 0
    q = -float("inf")
    for wi, vi in zip(w, v):
        if n >= wi:
            q = max(q, vi + fun(w, v, n - wi))
    return q


def bottom_up(w, v, n):
    table = [0] * (n + 1)
    for i in range(1, n + 1):
        q = -float("inf")
        for wi, vi in zip(w, v):
            if wi <= i:
                q = max(q, vi + table[i - wi])
        table[i] = q
    return table[-1]


w = [3, 2, 1, 4]
v = [33, 20, 5, 25]
print(fun(w, v, 4))
print(bottom_up(w, v, 4))
