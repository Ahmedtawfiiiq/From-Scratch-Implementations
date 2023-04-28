# function to find strongly connected components
def tarjanSCC_cycleDetection(g):
    unvisited = -1
    n = len(g)

    id = 0  # used to give each node an id
    sccCount = 0  # used to count number of strongly connected components in the graph

    ids = [0] * n
    low = [0] * n
    onStack = [False] * n
    stack = []
    scount = 0  # number of self loops in the graph
    for i in range(n):
        ids[i] = unvisited
    for i in range(n):
        if ids[i] == unvisited:
            # id = i
            low, sccCount, id, scount = dfs(
                i, g, id, ids, low, onStack, stack, sccCount, scount
            )
    # scc with 1 node is not counted
    count = 0  # number of nodes with more than 1 scc
    for i in range(n):
        label = i
        labelCount = 0
        for j in range(n):
            if low[j] == label:
                labelCount += 1
                if labelCount > 1:
                    count += 1
                    break
    # by default the algorithm finds all cycle
    # doesn't differentiate between self loops and scc with 1 node
    count += scount  # customized for detecting self loops

    return low, sccCount, count


def dfs(node, g, id, ids, low, onStack, stack, sccCount, scount):
    stack.append(node)
    onStack[node] = True
    ids[node] = low[node] = id
    id += 1

    # visit all neighbours and min low-link on callback
    for neighbour in g[node]:
        if neighbour == node:
            scount += 1
        if ids[neighbour] == -1:
            low, sccCount, id, scount = dfs(
                neighbour, g, id, ids, low, onStack, stack, sccCount, scount
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
    return low, sccCount, id, scount


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

g = {
    0: [10],
    3: [18],
    5: [5],  # self loop
    6: [11],
    11: [14],
    13: [1],
    15: [1],
    17: [4],
    1: [],
    2: [],
    4: [],
    7: [],
    8: [],
    9: [],
    10: [],
    12: [],
    14: [],
    16: [],
    18: [],
    19: [],
}


print("g:", g)
labels, n, count = tarjanSCC_cycleDetection(g)
print("labels:", labels)
print("number of scc:", n)
print("number of cycles:", count)
