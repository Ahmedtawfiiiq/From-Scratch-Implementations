def selectionSort(array):
    for i in range(len(array)):  # 0 -> n-1
        min = i
        for j in range(i, len(array)):
            if array[j] < array[min]:
                min = j
        array[i], array[min] = array[min], array[i]

    return array
