# all possible subarrays of an array
def array_subarrays(arr):
    n = len(arr)
    return [arr[i : j + 1] for i in range(n) for j in range(i, n)]


def string_subarrays(s):
    n = len(s)
    return [s[i : j + 1] for i in range(n) for j in range(i, n)]


a = [5, 6, 7, 8]
aa = array_subarrays(a)
print(aa)
print(len(aa))
s = "tree"
ss = string_subarrays(s)
print(ss)
