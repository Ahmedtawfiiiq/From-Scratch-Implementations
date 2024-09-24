def bounded_knapsack(w, v, n, W):
    if n == 0 or W == 0:
        return 0
    if W >= w[n - 1]:
        return max(
            v[n - 1] + bounded_knapsack(w, v, n - 1, W - w[n - 1]),
            bounded_knapsack(w, v, n - 1, W),
        )
    else:
        return bounded_knapsack(w, v, n - 1, W)


def bottom_up(w, v, n, W):
    table = [[0 for _ in range(n + 1)] for _ in range(W + 1)]
    for j in range(1, W + 1):
        for i in range(1, n + 1):
            if j >= w[n - i]:
                table[j][i] = max(
                    v[n - i] + table[j - w[n - i]][i - 1],
                    table[j][i - 1],
                )
            else:
                table[j][i] = table[j][i - 1]
    wi = W
    ni = n
    wights = []
    while wi > 0 and ni > 0:
        if table[wi][ni] != table[wi][ni - 1]:
            wights.append(w[n - ni])
            wi -= w[n - ni]
        ni -= 1
    return table[W][n], table, wights


# w = [3, 2, 1, 4]
# v = [33, 20, 5, 25]
# n = 4
# W = 4
w = [2, 3, 4, 7]
v = [70, 80, 90, 200]
W = 6
print(bounded_knapsack(w, v, len(w), W))
print(bottom_up(w, v, len(w), W))
