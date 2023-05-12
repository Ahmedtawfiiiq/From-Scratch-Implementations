from nodeClass import TreeNode


def dfs(root, inorder=[], preorder=[], postorder=[]):
    if not root:
        return
    preorder.append(root.val)
    dfs(root.left, inorder, preorder, postorder)
    inorder.append(root.val)
    dfs(root.right, inorder, preorder, postorder)
    postorder.append(root.val)
    return inorder, preorder, postorder


# BFS (level order traversal)
# make nodes at each level as a list
def bfs(root):
    if not root:
        return
    order = []
    queue = [root]
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.pop(0)
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        order.append(level)
    return order


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)
h = TreeNode(8)
i = TreeNode(9)
j = TreeNode(10)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
e.left = h
g.left = i
g.right = j

root = a

inorder, preorder, postorder = dfs(root)
print("Inorder  : ", inorder)
print("Preorder : ", preorder)
print("Postorder: ", postorder)
print("BFS      : ", bfs(root))
