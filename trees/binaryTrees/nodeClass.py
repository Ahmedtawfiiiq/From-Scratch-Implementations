class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(root, order=[]):
    if root is None:
        return
    order.append(root.val)
    dfs(root.left, order)
    dfs(root.right, order)
    return order


def dfs_stack(root):
    if root is None:
        return
    order = []
    stack = [root]
    while stack:
        node = stack.pop()
        order.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return order


a = TreeNode("a")
b = TreeNode("b")
c = TreeNode("c")
d = TreeNode("d")
e = TreeNode("e")
f = TreeNode("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

order = dfs(a)
print(order)
stack_order = dfs_stack(a)
print(stack_order)
