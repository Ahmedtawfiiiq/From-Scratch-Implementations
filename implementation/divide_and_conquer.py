# given array must be sorted array
def binarySearch(array, left, right, target):
    if left > right:
        return -1

    mid = (left + right) // 2

    if target == array[mid]:
        return mid

    if target > array[mid]:
        return binarySearch(array, mid + 1, right, target)
    else:
        return binarySearch(array, left, mid - 1, target)


# non optimized fibonacci series
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def mergeSort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2

    left = mergeSort(array[:mid])
    right = mergeSort(array[mid:])

    return merge(left, right)


def merge(left, right):
    i = 0
    j = 0
    k = 0
    temp = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            temp.append(left[i])
            i += 1
            k += 1
        else:
            temp.append(right[j])
            j += 1
            k += 1

    while i < len(left):
        temp.append(left[i])
        i += 1
        k += 1

    while j < len(right):
        temp.append(right[j])
        j += 1
        k += 1

    return temp


def quickSort(array, left, right):
    if left < right:
        b = partitioning(array, left, right)
        # left partition
        quickSort(array, left, b - 1)
        # right partition
        quickSort(array, b + 1, right)


def partitioning(array, left, right):
    pivot = array[right]
    b = left - 1
    i = left
    while i <= right:
        if array[i] > pivot:
            i += 1
        else:
            b += 1
            if array[b] >= pivot:
                array[b], array[i] = array[i], array[b]
            i += 1
    return b


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
# print(binarySearch(arr, 0, len(arr) - 1, 78))
# quickSort(arr, left=0, right=len(arr) - 1)
# print(arr)
print(countingSort(arr, max(arr)))
