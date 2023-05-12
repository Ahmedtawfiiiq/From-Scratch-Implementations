from nodeClass import TreeNode


# empty tree height is -1
# height of tree with one node is 0
def binaryTreeHeight(root, diameter):
    if not root:
        return -1
    lh = binaryTreeHeight(root.left, diameter)
    rh = binaryTreeHeight(root.right, diameter)
    diameter[0] = max(diameter[0], lh + rh + 2)
    return max(lh, rh) + 1


def diameterOfBinaryTree(root):
    diameter = [0]
    binaryTreeHeight(root, diameter)
    return diameter[0]


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)
h = TreeNode(8)
i = TreeNode(9)

a.left = b
a.right = c
c.left = d
d.left = e
e.left = f
c.right = g
g.right = h
h.right = i

root = a
print(diameterOfBinaryTree(root))
