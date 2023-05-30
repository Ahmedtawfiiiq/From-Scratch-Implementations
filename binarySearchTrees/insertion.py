from nodeClass import TreeNode, bfs


def insert(root, val):
    if root is None:
        return TreeNode(val)
    elif val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root


a = TreeNode(4)
b = TreeNode(2)
c = TreeNode(7)
d = TreeNode(1)
e = TreeNode(3)

a.left = b
a.right = c
b.left = d
b.right = e

val = 5

insert(a, val)
print(bfs(a))
