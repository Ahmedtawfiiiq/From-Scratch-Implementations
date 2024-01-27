# quick sort but not in place
def simpleQuickSort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        left = [x for x in array[1:] if x < pivot]
        right = [x for x in array[1:] if x >= pivot]
        return simpleQuickSort(left) + [pivot] + simpleQuickSort(right)


# 24 18 38 43 14 40 1 54
arr = [24, 18, 38, 43, 14, 40, 1, 54]
result = simpleQuickSort(arr)
for i in range(len(result)):
    print(result[i], end=" ")
