def countingSort(array, k):
    count = [0] * (k + 1)
    for i in range(len(array)):  # n
        count[array[i]] += 1

    for i in range(1, len(count)):  # k (n if k = O(n))
        count[i] += count[i - 1]

    output = [0] * len(array)
    for i in range(len(array) - 1, -1, -1):  # n
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1

    return output


arr = [5, 3, 2, 5, 4, 4, 5]
print(countingSort(arr, max(arr)))
