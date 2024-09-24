# recursive solution
def recursive_LCS(s1, s2, i, j):
    if i == 0 or j == 0:
        return 0
    if s1[i - 1] == s2[j - 1]:
        return 1 + recursive_LCS(s1, s2, i - 1, j - 1)
    else:
        return max(recursive_LCS(s1, s2, i - 1, j), recursive_LCS(s1, s2, i, j - 1))


def LCS(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    table = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if s1[i - 1] == s2[j - 1]:
                table[i][j] = 1 + table[i - 1][j - 1]
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])
    i = n1
    j = n2
    if type(s1[0]) is int:
        subsequence = []
    else:
        subsequence = ""
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            if type(s1[0]) is int:
                subsequence = [s1[i - 1]] + subsequence
            else:
                subsequence = s1[i - 1] + subsequence
            i -= 1
            j -= 1
        elif table[i - 1][j] > table[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return table[n1][n2], subsequence


# s1 = "ABCBDAB"
# s2 = "BDCAB"
# s1 = "ABCDEF"
# s2 = "ACFDEL"
s1 = [2, 3, 5, 1, 4, 7, 6]
s2 = sorted(s1)
# print(recursive_LCS(s1, s2, len(s1), len(s2)))
# print(LCS(s1, s2))
