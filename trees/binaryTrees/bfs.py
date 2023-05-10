from nodeClass import a


def bfs(root):
    if root is None:
        return
    order = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        order.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return order


order = bfs(a)
print(order)
