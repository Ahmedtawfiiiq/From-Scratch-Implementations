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


# quickSort(arr, left=0, right=len(arr) - 1)
# print(arr)
