# in-place
def bubbleSort(arr):
    n = len(arr)  # n = 5
    count = 0
    for i in range(n - 1):  # i:0->3
        isSwapped = False
        for j in range(n - 1, i, -1):  # i exclusive -> i:4->1
            count += 1
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                isSwapped = True
        if not isSwapped:
            break
    print(count)


arr = [1, 4, 3, 8, 7, 10]
bubbleSort(arr)
print(arr)
