# optimal game strategy for coin game
def fun(nums, i, j, memo):
    if (i, j) in memo:
        return memo[(i, j)]
    if i == j:
        return nums[i]
    if i + 1 == j:
        return max(nums[i], nums[j])
    memo[(i, j)] = max(
        nums[i] + min(fun(nums, i + 2, j, memo), fun(nums, i + 1, j - 1, memo)),
        nums[j] + min(fun(nums, i + 1, j - 1, memo), fun(nums, i, j - 2, memo)),
    )
    return memo[(i, j)]


def coins_game(coins):
    n = len(coins)
    memo = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        memo[i][i] = coins[i]
    for i in range(n - 1):
        memo[i][i + 1] = max(coins[i], coins[i + 1])
    for i in range(n - 2, -1, -1):
        for j in range(i + 2, n):
            memo[i][j] = max(
                coins[i] + min(memo[i + 2][j], memo[i + 1][j - 1]),
                coins[j] + min(memo[i + 1][j - 1], memo[i][j - 2]),
            )
    return memo[0][n - 1]


print("Alternate Turn Game")
nums = [5, 10, 100, 25]
print("Player 1 wins: ", fun(nums, 0, len(nums) - 1, {}))
print("Player 1 wins: ", coins_game(nums))
