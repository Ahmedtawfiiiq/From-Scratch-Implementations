# 1D dynamic programming
def bowling(pins):
    if len(pins) == 0:
        return 0
    if len(pins) == 1:
        return pins[0]
    dp = [-float("inf") for _ in range(len(pins))]
    dp[-1] = pins[-1]
    dp[-2] = max(pins[-2], pins[-2] * pins[-1])
    for i in range(len(pins) - 3, -1, -1):  # suffixes subproblems
        dp[i] = max(dp[i + 1], dp[i + 1] + pins[i], dp[i + 2] + (pins[i] * pins[i + 1]))
    return dp


# pins = [-3, 1, 1, 9, 9, 2, -5, -5]
pins = [-1, 1, 1, 1, 9, 9, 3, -3, -5, 2, 2]
print(bowling(pins))
