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
    # generate the solution
    solution = []
    while amount > 0:
        for coin in coins:
            if amount - coin >= 0 and n[amount] == 1 + n[amount - coin]:
                solution.append(coin)
                amount -= coin
                break
    return solution, n[-1]

def nWaysCoinChange(coins, amount):
    n = [0 for _ in range(amount + 1)]
    n[0] = 1
    for coin in coins:
        for j in range(coin, amount + 1):
            n[j] += n[j - coin]
    print(n)
    return n[-1]


coins = [1, 2, 5]
amount = 5
# print(fun(coins, amount))
print(bottom_up_coin_change(coins, amount))
print(nWaysCoinChange(coins, amount))
