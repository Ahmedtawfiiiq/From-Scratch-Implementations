def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_memo(n, memo={}):
    if n == 0 or n == 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


# time complexity: O(n)
# space complexity: O(n)
def tab_fib(n):
    table = [0] * (n + 1)
    table[1] = 1
    for i in range(n):
        table[i + 1] += table[i]
        if i + 1 < n:
            table[i + 2] += table[i] 
    return table[n]


# time complexity: O(n)
# space complexity: O(n)
def bottomUp_fib(n):
    table = [0] * (n + 1)
    table[1] = 1
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]
    return table[n]


import math


def fibonacci_golden_ratio(n):
    sqrt5 = math.sqrt(5)
    phi = (1 + sqrt5) / 2
    return round(phi**n / sqrt5)


print(fibonacci_golden_ratio(50))
print(fibonacci_memo(50))
