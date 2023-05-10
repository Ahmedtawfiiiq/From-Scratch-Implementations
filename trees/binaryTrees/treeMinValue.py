from nodeClass import TreeNode


def findMin(root):
    if root is None:
        return float("inf")
    return min(root.val, findMin(root.left), findMin(root.right))


def findMinStack(root):
    if root is None:
        return float("inf")
    stack = [root]
    minVal = float("inf")
    while stack:
        node = stack.pop()
        minVal = min(minVal, node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return minVal


a = TreeNode(5)
b = TreeNode(11)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(15)
f = TreeNode(12)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

print("recursive:", findMin(a))
print("iterative:", findMinStack(a))
