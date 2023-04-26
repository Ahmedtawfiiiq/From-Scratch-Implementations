def selectionSort(array):
    for i in range(len(array)):  # 0 -> n-1
        min = i
        for j in range(i, len(array)):
            if array[j] < array[min]:
                min = j
        array[i], array[min] = array[min], array[i]

    return array


def bubbleSort(array):
    # maximum of n passes to sort the array
    # each pass will move the largest element to the end
    # sorting at least 1 element each pass
    for i in range(len(array)):
        isSorted = True
        for j in range(len(array) - i - 1):
            if array[j + 1] < array[j]:
                array[j], array[j + 1] = array[j + 1], array[j]
                isSorted = False
        if isSorted:
            break
    return array


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
