# recursive with memoization
def fib_rec_memo(n, memo):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib_rec_memo(n - 1, memo) + fib_rec_memo(n - 2, memo)
    return memo[n]


# pull from the previous two values
def fib_pull(n):
    dp = {}
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]  # pulling from the previous two values
    return dp[n]


# push to the next two values
def fib_push(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(n):  # from 0 to n - 1
        # value of n can be reached from n - 1 and n - 2
        # so stop at n - 1 and only push to n
        # because n - 2 is already pushed to n and n - 1
        dp[i + 1] += dp[i]
        if i + 2 <= n:
            dp[i + 2] += dp[i]
    return dp[n]


print(fib_push(3))
