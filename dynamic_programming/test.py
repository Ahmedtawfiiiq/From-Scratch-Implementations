class Solution:
    def coinChange(self, coins, amount: int) -> int:
        n = len(coins)
        dp = [0 for _ in range(amount + 1)]
        for i in range(1, amount + 1):
            dp[i] = float("inf")
            for j in range(n):
                if i >= coins[j]:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)
        if dp[amount] == float("inf"):
            return -1
        else:
            return dp[amount]


if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    solution = Solution()
    print(solution.coinChange(coins, amount))
