def fun(s1, s2, i, j):
    if i == 0:
        return j
    if j == 0:
        return i
    if s1[i - 1] == s2[j - 1]:
        return fun(s1, s2, i - 1, j - 1)
    return 1 + min(
        fun(s1, s2, i - 1, j - 1),  # replace
        fun(s1, s2, i - 1, j),  # remove
        fun(s1, s2, i, j - 1),  # insert
    )


def bottom_up(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    table = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
    for i in range(n1):
        table[i][0] = i
    for j in range(n2):
        table[0][j] = j
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if s1[i - 1] == s2[j - 1]:
                table[i][j] = table[i - 1][j - 1]
            else:
                table[i][j] = 1 + min(
                    table[i][j - 1], table[i - 1][j], table[i - 1][j - 1]
                )
    return table[n1][n2]


s1 = "horse"
s2 = "ros"
print(bottom_up(s1, s2))
