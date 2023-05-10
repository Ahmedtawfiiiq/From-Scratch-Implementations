from nodeClass import a


# recursive solution
def dfs(root, order=[]):
    if root is None:
        return
    order.append(root.val)
    dfs(root.left, order)
    dfs(root.right, order)
    return order


# iterative solution
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


order = dfs(a)
print(order)
stack_order = dfs_stack(a)
print(stack_order)
