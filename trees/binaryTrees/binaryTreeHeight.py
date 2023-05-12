from nodeClass import TreeNode


# height of a binary tree is the number of edges
# in the longest path from the root node to a leaf node

# height of a given node is the number of edges
# in the longest path from the given node to a leaf node

# height of empty tree is -1
# height of tree with one node is 0


def binaryTreeHeight(root):
    if not root:
        return -1
    leftHeight = binaryTreeHeight(root.left)
    rightHeight = binaryTreeHeight(root.right)
    return max(leftHeight, rightHeight) + 1


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(6)
f = TreeNode(5)

a.left = b
a.right = c
c.left = d
c.right = e
d.left = f

root = a
print(binaryTreeHeight(root))
