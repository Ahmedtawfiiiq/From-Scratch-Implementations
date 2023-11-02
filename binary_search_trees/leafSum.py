from nodeClass import TreeNode


def leafSum(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return root.val
    return leafSum(root.left) + leafSum(root.right)


a = TreeNode(7)
b = TreeNode(4)
c = TreeNode(12)
d = TreeNode(2)
e = TreeNode(6)
f = TreeNode(9)
g = TreeNode(19)
h = TreeNode(3)
i = TreeNode(5)
j = TreeNode(8)
k = TreeNode(11)
l = TreeNode(15)
m = TreeNode(20)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
d.right = h
e.left = i
f.left = j
f.right = k
g.left = l
g.right = m

print(leafSum(a))
