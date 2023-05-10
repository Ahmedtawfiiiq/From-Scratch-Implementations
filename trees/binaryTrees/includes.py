from nodeClass import a


# dfs search
def treeSearch(root, target, order):
    if root is not None:
        order.append(root.val)
    if root is None:
        return False
    if root.val == target:
        return True
    return treeSearch(root.left, target, order) or treeSearch(root.right, target, order)


# bfs search
def treeSearchBFS(root, target):
    if root is None:
        return
    order = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        order.append(node.val)
        if node.val == target:
            return order, True
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return order, False


order = []
result = treeSearch(a, "e", order)
print(order, result)
print(treeSearchBFS(a, "e"))
