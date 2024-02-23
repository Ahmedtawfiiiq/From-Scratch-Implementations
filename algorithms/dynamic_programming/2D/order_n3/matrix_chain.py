def fun(p, i, j):
    if i == j:
        return 0
    q = float("inf")
    for k in range(i, j):
        q = min(
            q,
            (p[i] * p[k + 1] * p[j + 1]) + fun(p, i, k) + fun(p, k + 1, j),
        )
    return q


def bottom_up(p):
    n = len(p) - 1
    m = [[0 for _ in range(n)] for _ in range(n)]
    s = [[0 for _ in range(n)] for _ in range(n)]
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            q = float("inf")
            for k in range(i, j):
                result = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if result < q:
                    q = result
                    s[i][j] = k + 1
            m[i][j] = q
    return m[0][n - 1], s


def print_parenthesis(s, i, j):
    if i == j:
        return f"A{i}"
    return f"({print_parenthesis(s, i, s[i][j] - 1)}{print_parenthesis(s, s[i][j], j)})"


# p = [10, 100, 5, 50]
# p = [30, 35, 15, 5, 10]
# p = [40, 20, 30, 10, 30]
p = [10, 5, 20, 10, 5]
# p = [1, 3, 1, 4, 1, 5]
# print(fun(p, 0, len(p) - 2))
m, s = bottom_up(p)
print(m)
result = print_parenthesis(s, 0, len(p) - 2)
print(result)
