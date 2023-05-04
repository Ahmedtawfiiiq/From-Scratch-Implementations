
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


# unsorted arr
x  = [8, 4, 2, 5, 1, 3, 7, 6]
print(mergeSort(x))