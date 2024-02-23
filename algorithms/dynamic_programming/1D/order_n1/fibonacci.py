def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)


def bottom_up_fib(n):
    table = [0] * (n + 1)
    table[1] = 1
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]
    return table[n]


def top_down_fib(n, memo={}):
    if n == 0 or n == 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = top_down_fib(n - 1, memo) + top_down_fib(n - 2, memo)
    return memo[n]


def fib_golden_ratio(n):
    sqrt5 = 5**0.5
    phi = (1 + sqrt5) / 2
    return round(phi**n / sqrt5)
