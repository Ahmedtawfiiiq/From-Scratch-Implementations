from collections import defaultdict
from nodeClass import TreeNode


def dfsRecursive(graph, start, arrangement):
    while graph[start]:
        next_node = graph[start].pop()
        dfsRecursive(graph, next_node, arrangement)
    arrangement.append(start)


def eulerianPath(pairs, root):
    start = root  # assume eulerian circuit
    graph = defaultdict(list)
    count = defaultdict(int)
    for pair in pairs:
        graph[pair[0]].append(pair[1])
        count[pair[0]] += 1
        count[pair[1]] -= 1
    for key in count:  # eulerian path check
        if count[key] == 1:
            start = key
            break
    arrangement = []
    dfsRecursive(graph, start, arrangement)
    return arrangement[::-1]


def findDepth(root):
    depth = defaultdict(int)
    stack = [[root, 0]]
    while stack:
        node, d = stack.pop()
        depth[node] = d
        if node.left:
            stack.append([node.left, d + 1])
        if node.right:
            stack.append([node.right, d + 1])
    return depth


def toUndirected(root):
    edgeList = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node.left:
            edgeList.append([node, node.left])
            edgeList.append([node.left, node])
            stack.append(node.left)
        if node.right:
            edgeList.append([node, node.right])
            edgeList.append([node.right, node])
            stack.append(node.right)
    return edgeList


def lowestCommonAncestor(root, p, q):
    d = findDepth(root)
    edgeList = toUndirected(root)
    tour = eulerianPath(edgeList, root)
    depth = [0 for _ in range(len(tour))]
    for i in range(len(tour)):
        depth[i] = d[tour[i]]
    p_index = -1
    q_index = -1
    for i in range(len(tour) - 1, -1, -1):
        if tour[i] == p:
            p_index = i
        if tour[i] == q:
            q_index = i
        if p_index != -1 and q_index != -1:
            break
    minimum = float("inf")
    index = -1
    for i in range(min(p_index, q_index), max(p_index, q_index) + 1):
        if depth[i] < minimum:
            minimum = depth[i]
            index = i
    return tour[index]


root = TreeNode(3)
a = TreeNode(5)
b = TreeNode(1)
c = TreeNode(6)
d = TreeNode(2)
e = TreeNode(0)
f = TreeNode(8)
g = TreeNode(7)
h = TreeNode(4)

root.left = a
root.right = b
a.left = c
a.right = d
b.left = e
b.right = f
d.left = g
d.right = h

p = 5
q = 1
lca = lowestCommonAncestor(root, p, q)
print(lca.val)
