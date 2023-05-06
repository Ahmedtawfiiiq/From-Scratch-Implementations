def remove_all(l, n1, n2):
    if len(l) == 0:
        return []
    elif l[0] == n1 or l[0] == n2:
        return remove_all(l[1:], n1, n2)
    else:
        return [l[0]] + remove_all(l[1:], n1, n2)


def fun(arr, index):
    if len(arr) == 0 or len(arr) == 1:
        return 0
    v = arr[index]
    del arr[index]
    arr = remove_all(arr, v - 1, v + 1)
    s = 0
    for i in range(len(arr)):
        s = max(s, arr[i] + fun(arr.copy(), i))
    return s


nums = [3, 4, 2]
r = 0
for i in range(len(nums)):
    r = max(r, nums[i] + fun(nums.copy(), i))
print(r)
