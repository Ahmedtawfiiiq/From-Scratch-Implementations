def count_partitions(n, m):
    if n == 0:
        return 1
    if m == 0 or n < 0:
        return 0
    return count_partitions(n, m - 1) + count_partitions(n - m, m)


print(count_partitions(5, 5))
