from nodeClass import TreeNode


# maximum depth of a binary tree
# is the number of nodes along the longest path
# from the root node down to the farthest leaf node
def maxDepth(root):
    if not root:
        return 0
    leftHeight = maxDepth(root.left)
    rightHeight = maxDepth(root.right)
    return max(leftHeight, rightHeight) + 1


# minimum depth of a binary tree
# is the number of nodes along the shortest path
# from the root node down to the nearest leaf node
def minDepth(root):
    if not root:
        return 0
    leftHeight = minDepth(root.left)
    rightHeight = minDepth(root.right)
    if leftHeight == 0 or rightHeight == 0:
        return max(leftHeight, rightHeight) + 1
    return min(leftHeight, rightHeight) + 1


# a = TreeNode(2)
# b = TreeNode(3)
# c = TreeNode(4)
# d = TreeNode(5)
# e = TreeNode(6)

# a.right = b
# b.right = c
# c.right = d
# d.right = e

a = TreeNode(15)

root = a
# print(maxDepth(None))
# print(minDepth(root))
