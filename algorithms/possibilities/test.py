def fun(s1, s2, n1, n2):
    t1 = {""}
    t2 = {""}
    for i in range(n1):
        current = {s1[i] + sub for sub in t1}
        t1 = t1.union(current)
    for i in range(n2):
        current = {s2[i] + sub for sub in t2}
        t2 = t2.union(current)
    subsequences = t1.intersection(t2)
    # print longest common subsequence
    return max(subsequences, key=len)
    # return subsequences


s1 = "ABCBDAB"
s1 = [c for c in s1]
s2 = "BDCAB"
s2 = [c for c in s2]
n1 = len(s1)
n2 = len(s2)
common = fun(s1, s2, n1, n2)
print(common)
