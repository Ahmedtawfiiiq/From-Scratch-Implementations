# def freqTable(arr):
#     freq = {}
#     for i in arr:
#         if i in freq:
#             freq[i] += 1
#         else:
#             freq[i] = 1
#     return freq


# # function to remove duplicates from an array
# def removeDuplicates(arr):
#     freq = freqTable(arr)
#     result = []
#     for key in freq:
#         result.append(key)
#     return result


# def fun(arr, freq):
#     if arr == []:
#         return 0
#     m = 0
#     for element in arr:
#         c = arr.copy()
#         c.remove(element)
#         if element - 1 in c:
#             c.remove(element - 1)
#         if element + 1 in c:
#             c.remove(element + 1)
#         m = max(m, element*freq[element] + fun(c, freq))
#     return m

# nums = [2, 2, 3, 3, 3, 4]
# table = freqTable(nums)
# d = removeDuplicates(nums)
# print(fun(d, table))

