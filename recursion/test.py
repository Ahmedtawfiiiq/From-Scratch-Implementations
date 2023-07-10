def fun(nums):
    result = set()
    nums.sort()
    n = len(nums)
    for k, v in enumerate(nums):
        i = k + 1
        j = n - 1
        for l in range(k + 1, n):
            if i == j:
                continue
            twosum = nums[i] + nums[j]
            if v + twosum == 0:
                result.add((v, nums[i], nums[j]))
                i += 1
                j -= 1
            elif v + twosum > 0:
                j -= 1
            else:
                i += 1
    r = []
    for ele in result:
        r.append(list(ele))
    return r


nums = [-2, 0, 1, 1, 2]
print(fun(nums))
