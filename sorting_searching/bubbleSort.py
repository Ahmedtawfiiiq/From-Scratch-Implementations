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
