from nodeClass import TreeNode


def totalSum(root):
    if root is None:
        return 0
    return root.val + totalSum(root.left) + totalSum(root.right)


# iterative solution
def totalSumStack(root):
    if root is None:
        return 0
    sum = 0
    stack = [root]
    while stack:
        node = stack.pop()
        sum += node.val
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return sum


a = TreeNode(3)
b = TreeNode(11)
c = TreeNode(4)
d = TreeNode(4)
e = TreeNode(2)
f = TreeNode(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

print("recursive:", totalSum(a))
print("iterative:", totalSumStack(a))
