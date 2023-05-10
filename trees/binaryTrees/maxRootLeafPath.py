from nodeClass import TreeNode


def findMaxPath(root):
    if root is None:
        return 0
    return root.val + max(findMaxPath(root.left), findMaxPath(root.right))


a = TreeNode(5)
b = TreeNode(11)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(2)
f = TreeNode(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

print(findMaxPath(a))
