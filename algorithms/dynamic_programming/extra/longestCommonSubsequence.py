import numpy as np


import numpy as np


# recursive solution with memoization
def LCS_recursive(A, B, memo, m, n):
    if memo[m][n] != -1:
        return memo[m][n]
    if A == "" or B == "":
        return 0
    if A[0] == B[0]:
        memo[m][n] = 1 + LCS_recursive(A[1:], B[1:], memo, m - 1, n - 1)
        return memo[m][n]
    else:
        memo[m][n] = max(
            LCS_recursive(A[1:], B, memo, m - 1, n),
            LCS_recursive(A, B[1:], memo, m, n - 1),
        )
        return memo[m][n]


# using prefixes
def LCS(A, B):
    # length + 1 to consider empty sequences
    n = len(A) + 1
    m = len(B) + 1
    dp = np.zeros((n, m))
    for i in range(1, n):
        for j in range(1, m):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp


def LCS_suffixes(A, B):
    # length + 1 to consider empty sequences
    n = len(A) + 1
    m = len(B) + 1
    dp = np.zeros((n, m))
    for i in range(n - 2, -1, -1):
        for j in range(m - 2, -1, -1):
            if A[i] == B[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
    return dp.astype(int)


def findSubsequence(dp, A):
    r = len(dp) - 1  # length of string A
    c = len(dp[0]) - 1  # length of string B
    subsequence = ""
    i = 0
    j = 0
    while i < r and j < c:
        if dp[i][j] > dp[i][j + 1] and dp[i][j] > dp[i + 1][j]:
            subsequence += A[i]
            # move diagonally
            i += 1
            j += 1
        elif dp[i][j + 1] > dp[i + 1][j]:
            j += 1  # move to the right
        else:
            i += 1  # move to the down
    return subsequence


s2 = "their"
s1 = "habit"
# s1 = "bdcaba"
# s2 = "abcbdab"
dp = LCS_suffixes(s1, s2)
# print(l)
# print(dp)
sequence = findSubsequence(dp, s1)
print(sequence)

# recursive solution
# m = len(s1)
# n = len(s2)
# memo = [[-1 for i in range(n + 1)] for j in range(m + 1)]
# result = LCS_recursive(s1, s2, memo, m, n)
# print(result)
