# function to find strongly connected components
def tarjanSCC(g):
    unvisited = -1
    n = len(g)

    id = 0  # used to give each node an id
    sccCount = 0  # used to count number of strongly connected components in the graph

    ids = [0] * n
    low = [0] * n
    onStack = [False] * n
    stack = []
    for i in range(n):
        ids[i] = unvisited
    for i in range(n):
        if ids[i] == unvisited:
            # id = i
            low, sccCount, id = dfs(i, g, id, ids, low, onStack, stack, sccCount)
    return low, sccCount


def dfs(node, g, id, ids, low, onStack, stack, sccCount):
    stack.append(node)
    onStack[node] = True
    ids[node] = low[node] = id
    id += 1

    # visit all neighbours and min low-link on callback
    for neighbour in g[node]:
        if ids[neighbour] == -1:
            low, sccCount, id = dfs(
                neighbour, g, id, ids, low, onStack, stack, sccCount
            )
        if onStack[neighbour]:
            low[node] = min(low[node], low[neighbour])
    #  after having visited all the neighbours of node
    #  if low-link of node is equal to id of node
    #  then we have found a strongly connected component
    if ids[node] == low[node]:
        while stack[-1] != node:
            w = stack.pop()
            onStack[w] = False
            low[w] = ids[node]
        w = stack.pop()
        onStack[w] = False
        low[w] = ids[node]
        sccCount += 1
    return low, sccCount, id


g = {
    0: [1],
    1: [2],
    2: [0],
    3: [4, 7],
    4: [5],
    5: [6, 0],
    6: [0, 2, 4],
    7: [3, 5],
}

# g = {
#     0: [2, 3],
#     1: [0],
#     2: [1],
#     3: [4],
#     4: [],
# }

labels, n = tarjanSCC(g)
print("labels:", labels)
print("n:", n)
