class Solution:
    def rob(self, nums):
        i = 0
        j = 0
        for n in nums:
            result = max(i + n, j)
            i = j
            j = result
        return j



arr = [1, 2, 3, 1]
print(Solution().rob(arr))
