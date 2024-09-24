from nodeClass import TreeNode


# counts the number of nodes in a BSTs
def count1(root):
    if root == None:
        return 0
    return 1 + count1(root.left) + count1(root.right)


# counts the number of nodes in a BST containing
# values that are >= to a certain value
def count2(root, val):
    if root == None:
        return 0
    if root.val >= val:
        return 1 + count2(root.left, val) + count2(root.right, val)
    return count2(root.right, val)


# counts the number of nodes with even values
def count3(root):
    if root == None:
        return 0
    if root.val % 2 == 0:
        return 1 + count3(root.left) + count3(root.right)
    return count3(root.left) + count3(root.right)



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
