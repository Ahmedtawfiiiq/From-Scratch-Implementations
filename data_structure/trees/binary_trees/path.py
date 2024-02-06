from nodeClass import TreeNode


# function to find the path from root to a given value
def findPath(root, value):
    if root is None:
        return []
    if root.val == value:
        return [root.val]
    leftPath = findPath(root.left, value)
    rightPath = findPath(root.right, value)
    if leftPath:
        return [root.val] + leftPath
    if rightPath:
        return [root.val] + rightPath
    return []


# function to find all paths from root to a leaf node
# that sum to a given value
def findAllPaths(root, value):
    if root is None:
        return []
    if root.val == value and root.left is None and root.right is None:
        return [[root.val]]
    leftPath = findAllPaths(root.left, value - root.val)
    rightPath = findAllPaths(root.right, value - root.val)
    result = []
    for path in leftPath + rightPath:
        result.append([root.val] + path)
    return result
    # return [[root.val] + path for path in leftPath + rightPath]


def allLeafPaths(root):
    if root is None:
        return []
    if root.left is None and root.right is None:
        return [[root.val]]
    leftPath = allLeafPaths(root.left)
    rightPath = allLeafPaths(root.right)
    result = []
    lr = leftPath + rightPath  # each represent a different path list
    for path in lr:
        result.append([root.val] + path)
    return result
    # return [[root.val] + path for path in leftPath + rightPath]


a = TreeNode(5)
b = TreeNode(4)
c = TreeNode(8)
d = TreeNode(11)
e = TreeNode(13)
f = TreeNode(4)
g = TreeNode(7)
h = TreeNode(2)
i = TreeNode(5)
j = TreeNode(1)

a.left = b
a.right = c
b.left = d
c.left = e
c.right = f
d.left = g
d.right = h
f.left = i
f.right = j

root = a

# print(findPath(root, 5))
# print(findPath(root, 1))

# print(findAllPaths(root, 22))

print(allLeafPaths(root))
