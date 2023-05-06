# 1D dynamic programming
def rodCutting(p, n):
    size = len(p)
    dp = [0] * size
    for i in range(1, size):
        for j in range(i, 0, -1):  # suffixes [i:]
            value = p[j] + dp[i - j]
            if value > dp[i]:
                dp[i] = value
    return dp[n], dp


p = [0, 1, 5, 8, 9, 10, 17, 17, 20]
print(rodCutting(p, 8))
