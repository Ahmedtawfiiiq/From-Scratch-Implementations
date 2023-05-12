from nodeClass import TreeNode


# function to find all paths from root to a leaf node
# that sum to a given value
def findPath(root, value):
    if root is None:
        return []
    if root.val == value and root.left is None and root.right is None:
        return [[root.val]]
    leftPath = findPath(root.left, value - root.val)
    rightPath = findPath(root.right, value - root.val)
    return [[root.val] + path for path in leftPath + rightPath]


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

print(findPath(root, 22))
