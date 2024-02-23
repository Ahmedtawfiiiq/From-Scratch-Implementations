def fun(coins, amount):
    if amount == 0:
        return 0
    q = float("inf")
    for j in range(len(coins)):
        if amount - coins[j] >= 0:
            q = min(q, 1 + fun(coins, amount - coins[j]))
    return q


def bottom_up_coin_change(coins, amount):
    n = [0 for _ in range(amount + 1)]
    for j in range(1, amount + 1):
        q = float("inf")
        for coin in coins:
            if j - coin >= 0:
                q = min(q, 1 + n[j - coin])
        n[j] = q
    return n[amount]


coins = [1, 3, 4]
amount = 6
print(fun(coins, amount))
print(bottom_up_coin_change(coins, amount))
