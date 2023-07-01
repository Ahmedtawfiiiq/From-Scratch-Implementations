# return index of target in array, if not found return -1
def binarySearch(array, left, right, target):
    if left > right:
        return left

    mid = (left + right) // 2

    if target == array[mid]:
        return mid

    if target > array[mid]:
        return binarySearch(array, mid + 1, right, target)  # update left and keep right
    else:
        return binarySearch(array, left, mid - 1, target)  # update right and keep left


def binarySearchIterative(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2

        if target == arr[mid]:
            return mid

        if target > arr[mid]:  # update left and keep right
            left = mid + 1
        else:
            right = mid - 1  # update right and keep left
    return -1


arr = ["c", "f", "j"]
target = "a"

# given array must be sorted array
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
index = binarySearch(arr, 0, len(arr) - 1, target)
# print(binarySearchIterative(arr, 8))

print(index)
