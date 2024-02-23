def binary_search(array, left, right, target):
    if left > right:
        # where the target should be inserted
        return left

    mid = (left + right) // 2

    if target == array[mid]:
        return mid

    if target > array[mid]:
        return binary_search(array, mid + 1, right, target)
    else:
        return binary_search(array, left, mid - 1, target)


def lis_strictly_increasing(arr):
    sequence = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] > sequence[-1]:
            sequence.append(arr[i])
        else:
            index = binary_search(sequence, 0, len(sequence) - 1, arr[i])
            sequence[index] = arr[i]
    return len(sequence)


def lis(arr):
    n = len(arr)
    table = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                table[i] = max(table[i], table[j] + 1)
    print(table)
    return max(table)


def foo(arr, n):
    result = 1
    for i in range(2, n + 1):
        q = 0
        for j in range(i - 2, -1, -1):
            if arr[i - 1] > arr[j]:
                q = max(q, foo(arr, j + 1) + 1)
        result = max(result, q)
    return result


l = [4, 10, 4, 3, 8, 9]
# print(lis_strictly_increasing(l))
# print(lis(l))
print(foo(l, len(l)))
