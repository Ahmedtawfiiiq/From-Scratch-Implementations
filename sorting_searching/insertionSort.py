def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i
        while arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
            if j == 0:
                break


arr = [3, 5, 4, 3, 2, 1]
insertionSort(arr)
print(arr)
