# in-place
def selectionSort(arr):
    n = len(arr)  # n = 5
    for i in range(n - 1):  # i:0->3
        min = i
        for j in range(n - 1, i, -1):  # j:4->1
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]


arr = [8, 2, 4, 1, 3]
selectionSort(arr)
print(arr)
