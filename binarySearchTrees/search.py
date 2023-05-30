from nodeClass import TreeNode


def search(root, val):
    if root is None:
        return None
    elif root.val == val:
        return root
    elif val < root.val:
        return search(root.left, val)
    else:
        return search(root.right, val)


a = TreeNode(4)
b = TreeNode(2)
c = TreeNode(7)
d = TreeNode(1)
e = TreeNode(3)

a.left = b
a.right = c
b.left = d
b.right = e

print(search(a, 2))
