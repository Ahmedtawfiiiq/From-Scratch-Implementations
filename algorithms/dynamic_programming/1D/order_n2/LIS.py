def fun(arr, n):
    if n == 0:
        return 1
    result = 1
    for i in range(n - 1, -1, -1):
        if arr[n] > arr[i]:
            result = max(result, 1 + fun(arr, i))
    return result


def recursive(arr, n):
    result = 1
    for i in range(n):
        result = max(result, fun(arr, i))
    return result


def bottom_up(arr):
    n = len(arr)
    table = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                table[i] = max(table[i], table[j] + 1)
    max_length = max(table)
    result = [arr[i] for i in range(n - 1, -1, -1) if table[i] == max_length and (max_length := max_length - 1) >= 0]
    return result[::-1]


l = [3, 10, 2, 11]
print(bottom_up(l))
print(recursive(l, len(l)))
