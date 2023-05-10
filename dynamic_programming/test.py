def fun(l, n, memo):
    if n in memo:
        return memo[n]
    if len(l) == 2:
        return max(l[0], l[1])
    if n >= len(l):
        return 0
    r = 0
    for i in range(2, len(l)):
        r = max(r, l[n] + fun(l, n + i, memo))
    memo[n] = r
    return memo[n]


def solve(nums):
    if len(nums) == 1:
        return nums[0]
    r = 0
    r = max(r, fun(nums[:-1], 0, {}))
    r = max(r, fun(nums[1:], 0, {}))
    for i in range(1, len(nums)):
        r = max(r, fun(nums, i, {}))
    return r


def freqTable(arr, freq):
    for i in arr:
        freq[i] += i
    return freq


nums = [3, 4, 2]
freq = [0 for _ in range(max(nums) + 1)]
arr = freqTable(nums, freq)
result = solve(arr)
print(result)
