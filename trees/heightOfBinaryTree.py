def fun(t, root):
    if t[root] == []:
        print(root, end=" ")
        return 0
    s = 0
    for child in t[root]:
        h = 1 + fun(t, child)
        s = max(s, h)
    return s


def binaryTreeHeight(t, root):
    if t[root] == []:
        return 0
    if len(t[root]) == 1:
        return binaryTreeHeight(t, t[root][0]) + 1  # if there is only one child
    else:
        # if there are two children
        return max(binaryTreeHeight(t, t[root][0]), binaryTreeHeight(t, t[root][1])) + 1


t = {
    5: [4, 3],
    4: [1, -6],
    3: [0, -4],
    1: [2, 9],
    -6: [],
    0: [],
    -4: [],
    2: [],
    9: [7],
    7: [],
}

# result = fun(t, 5)
# print("\nheight:", result) # height of any tree

# height of a binary tree
result = binaryTreeHeight(t, 5)
print("height:", result)  # height of a binary tree
