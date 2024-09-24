import random

def partition(array, left, right):
    # pivot = array[right]
    pivot = array[random.randint(left, right)]
    p = left - 1
    i = left
    while i <= right:
        if array[i] <= pivot:
            p += 1
            if array[p] >= pivot:
                array[p], array[i] = array[i], array[p]
        i += 1
    return p


def quick_Select(arr, l, r, k):
    if l < r:
        p = partition(arr, l, r)
        if p == k:
            return arr[p]
        elif k < p:
            return quick_Select(arr, l, p - 1, k)
        else:
            return quick_Select(arr, p + 1, r, k)


# negative before positive
def fun(arr):
    n = len(arr)
    pivot = 0
    p = -1
    for i in range(n):
        if arr[i] <= pivot:
            p += 1
            if arr[p] >= pivot:
                arr[p], arr[i] = arr[i], arr[p]


def quickSort(array, left, right):
    if left < right:
        p = partition(array, left, right)
        quickSort(array, left, p - 1)
        quickSort(array, p + 1, right)


def stack_quick_sort(arr, l, r):
    stack = [(l, r)]
    while stack:
        l, r = stack.pop(-1)
        if l < r:
            p = partition(arr, l, r)
            stack.append((l, p - 1))
            stack.append((p + 1, r))


def get_median(arr, l, r):
    n = r - l + 1
    k = n // 2
    if n % 2 != 0:  # odd length -> get the middle element
        return quick_Select(arr, l, r, k)
    else:
        return (quick_Select(arr, l, r, k) + quick_Select(arr, l, r, k - 1)) / 2


# quickSort(arr, left=0, right=len(arr) - 1)
# print(arr)

arr = [2, 3, -2, 5, -4, 7, 0]
n = len(arr)
# fun(arr)
# stack_quick_sort(arr, 0, n - 1)
# quickSort(arr, left=0, right=len(arr) - 1)
# print(arr)
# p = partition(arr, 0, n - 1)
m = get_median(arr, 0, n - 1)
print(m)
# print(p, arr)
