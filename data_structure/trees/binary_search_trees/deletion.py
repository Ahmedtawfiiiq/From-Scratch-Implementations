from nodeClass import TreeNode, bfs


# recursive
def findSmallest(root):
    if root.left is None:
        return root
    return findSmallest(root.left)


def deletion(root, val):
    if not root:
        return None
    if root.val == val:
        if not root.left and not root.right:  # has no children
            return None
        elif not root.left:  # has only right child
            return root.right
        elif not root.right:  # has only left child
            return root.left
        else:  # has both left and right children
            # find the smallest value in the right subtree
            smallest = findSmallest(root.right)
            # replace the root value with the smallest value
            root.val = smallest.val
            # delete the smallest value in the right subtree
            root.right = deletion(root.right, smallest.val)
    elif root.val > val:
        root.left = deletion(root.left, val)
    else:
        root.right = deletion(root.right, val)
    return root


a = TreeNode(9)
b = TreeNode(5)
c = TreeNode(12)
d = TreeNode(2)
e = TreeNode(7)
f = TreeNode(10)
g = TreeNode(13)
h = TreeNode(1)
i = TreeNode(3)
j = TreeNode(6)
k = TreeNode(8)
l = TreeNode(4)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
d.left = h
d.right = i
e.left = j
e.right = k
i.left = l


print(bfs(a))
deletion(a, 5)
print(bfs(a))
