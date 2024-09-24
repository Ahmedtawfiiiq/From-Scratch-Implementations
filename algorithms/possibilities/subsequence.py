def string_subsequences(s, n):
    if n == 0:
        return [""]
    exclude = string_subsequences(s, n - 1)
    include = [s[n - 1] + sub for sub in exclude]
    return include + exclude


def array_subsequences(arr, n):
    if n == 0:
        return [[]]
    exclude = array_subsequences(arr, n - 1)
    include = [[arr[n - 1]] + sub for sub in exclude]
    return include + exclude


def bottom_up(arr):
    n = len(arr)
    subsequences = [[]]
    for i in range(n):
        subsequences += [sub + [arr[i]] for sub in subsequences]
    return subsequences


s = "abc"
# ss = string_subsequences(s, len(s))
# print(ss)
# print(len(ss))
a = [5, 6, 7, 8]
# aa = array_subsequences(a, len(a))
# print(aa)
# print(len(aa))
aa = bottom_up(a)
print(aa)
print(len(aa))

