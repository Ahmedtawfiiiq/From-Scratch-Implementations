def fun(n):
    if n == 0:
        return 1
    q = 0
    for k in range(n):
        q += fun(k) * fun(n - 1 - k)
    return q


def bottom_up(n):
    table = [0] * (n + 1)
    table[0] = table[1] = 1
    for i in range(2, n + 1):
        for j in range(i // 2):
            table[i] += table[j] * table[i - 1 - j] * 2
        if i % 2 == 1:
            table[i] += table[i // 2] * table[i // 2]
    return table[n]


for i in range(3, 11):
    print(bottom_up(i))
