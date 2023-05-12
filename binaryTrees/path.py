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


a = TreeNode(3)
b = TreeNode(5)
c = TreeNode(1)
d = TreeNode(6)
e = TreeNode(2)
f = TreeNode(0)
g = TreeNode(8)
h = TreeNode(7)
i = TreeNode(4)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
e.left = h
e.right = i

root = a

print(findPath(root, 5))
print(findPath(root, 1))
