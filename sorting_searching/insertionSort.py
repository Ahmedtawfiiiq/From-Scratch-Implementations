def insertionSort(array):
    for i in range(1, len(array)):
        current = array[i]
        j = i - 1
        while j >= 0 and array[j] > current:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = current
    return array


unsorted = [3, 5, 4, 3, 2, 1]
sorted = insertionSort(unsorted)
print(sorted)
