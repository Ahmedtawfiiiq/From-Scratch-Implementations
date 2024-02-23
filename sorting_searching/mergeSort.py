def merge(arr, left, mid, right):
    temp = []
    i = left
    j = mid + 1
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
    while i <= mid:
        temp.append(arr[i])
        i += 1
    while j <= right:
        temp.append(arr[j])
        j += 1
    for i in range(left, right + 1):
        arr[i] = temp[i - left]


def mergeSort(arr, l, r):
    if l < r:
        mid = (l + r) // 2
        mergeSort(arr, l, mid)
        mergeSort(arr, mid + 1, r)
        merge(arr, l, r)


arr = [8, 4, 2, 5, 1, 3, 7, 6]
n = len(arr)
mergeSort(arr, 0, n - 1)
print(arr)
