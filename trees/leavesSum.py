def fun(t, root):
    if t[root] == []:
        print(root, end=" ")
        return root
    s = 0
    for child in t[root]:
        s += fun(t, child)
    return s


t = {
    5: [4, 3],
    4: [1, -6],
    3: [0, 7, -4],
    1: [2, 9],
    -6: [],
    0: [],
    7: [8],
    -4: [],
    2: [],
    9: [],
    8: [],
}
result = fun(t, 5)
# summation of leaf nodes
print("\nsummation:", result)
