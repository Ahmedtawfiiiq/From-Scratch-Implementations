def longestIncreasingSubsequence(l):
    table = [1] * len(l)
    prev = [None] * len(l)
    for i in range(1, len(l)):
        for j in range(i):
            # just add the equal sign to make it non-decreasing
            if l[j] < l[i] and table[j] + 1 > table[i]:
                table[i] = table[j] + 1
                prev[i] = j
    max_index = table.index(max(table))
    lis = []
    while max_index is not None:
        lis.append(l[max_index])
        max_index = prev[max_index]
    lis.reverse()
    return lis, max(table)


l = [3, 1, 1, 8, 2, 5]
# l = "empathy"
# find the longest increasing subsequence
print(longestIncreasingSubsequence(l)) 
