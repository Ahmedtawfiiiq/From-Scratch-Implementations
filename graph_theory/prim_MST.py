from heapq import heappop, heappush
from graph_theory.Ageneral import adjacencyListToTuplesList, directed_to_undirected


def primTupleList(tupleList):
    for i in range(len(tupleList)):
        for j in range(len(tupleList[i])):
            neighbour, weight = tupleList[i][j]
            tupleList[i][j] = (i, weight, neighbour)
    return tupleList


def primMST(graph, source):
    V = len(graph)
    visited = set()
    queue = [(0, source, source)]  # (weight, parent, node)
    mst = []  # parent, node, weight
    while len(mst) < V and queue:
        weight, parent, node = heappop(queue)
        if node not in visited:
            visited.add(node)
            mst.append((parent, node, weight))
            for parent, weight, neighbour in graph[node]:
                if neighbour not in visited:
                    heappush(queue, (weight, parent, neighbour))
    cost = sum([w for _, _, w in mst])
    return mst, cost


adjacencyMatrix = [
    [0, 10, 1, 4, 0, 0, 0, 0],
    [10, 0, 3, 0, 0.1, 0, 0, 0],
    [1, 3, 0, 2, 0, 8, 0, 0],
    [4, 0, 2, 0, 0, 2, 7, 0],
    [0, 0.1, 0, 0, 0, 1, 0, 8],
    [0, 0, 8, 0, 1, 0, 6, 9],
    [0, 0, 0, 7, 0, 6, 0, 12],
    [0, 0, 0, 0, 8, 9, 12, 0],
]


adjacencyList = {
    "0": {"1": 10, "2": 1, "3": 4},
    "1": {"0": 10, "2": 3, "4": 0},
    "2": {"0": 1, "1": 3, "3": 2, "5": 8},
    "3": {"0": 4, "2": 2, "5": 2, "6": 7},
    "4": {"1": 0, "5": 1, "7": 8},
    "5": {"2": 8, "4": 1, "6": 6, "7": 9},
    "6": {"3": 7, "5": 6, "7": 12},
    "7": {"4": 8, "5": 9, "6": 12},
}

# parent, weight, node
tupleList = [
    [(0, 10, 1), (0, 1, 2), (0, 4, 3)],
    [(1, 10, 0), (1, 3, 2), (1, 0, 4)],
    [(2, 1, 0), (2, 3, 1), (2, 2, 3), (2, 8, 5)],
    [(3, 4, 0), (3, 2, 2), (3, 2, 5), (3, 7, 6)],
    [(4, 0, 1), (4, 1, 5), (4, 8, 7)],
    [(5, 8, 2), (5, 1, 4), (5, 6, 6), (5, 9, 7)],
    [(6, 7, 3), (6, 6, 5), (6, 12, 7)],
    [(7, 8, 4), (7, 9, 5), (7, 12, 6)],
]

test = {
    "0": {"1": 9, "2": 5, "3": 2},
    "1": {"0": 9, "3": 6, "4": 5},
    "2": {"0": 5, "3": 4, "4": 5},
    "3": {"0": 2, "1": 6, "2": 4, "4": 4},
    "4": {"1": 5, "2": 5, "3": 4},
}

xx = adjacencyListToTuplesList(test)
xxx = primTupleList(xx)
print(xxx)
print(primMST(xxx, 0))
