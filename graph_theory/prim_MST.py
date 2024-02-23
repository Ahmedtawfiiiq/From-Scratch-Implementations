from heapq import heappop, heappush
from Ageneral import adjacencyListToTuplesList, directed_to_undirected


def primTupleList(tupleList):
    for i in range(len(tupleList)):
        for j in range(len(tupleList[i])):
            neighbour, weight = tupleList[i][j]
            tupleList[i][j] = (i, weight, neighbour)
    return tupleList


def primMST(graph, source, isMax=False):
    V = len(graph)
    visited = set()
    queue = [(0, source, source)]  # (weight, parent, node)
    mst = []  # parent, node, weight
    while len(mst) < V and queue:
        weight, parent, node = heappop(queue)
        if node not in visited:
            visited.add(node)
            if isMax:
                weight = -weight
            mst.append((parent, node, weight))
            for parent, weight, neighbour in graph[node]:
                if neighbour not in visited:
                    if isMax:
                        weight = -weight
                    heappush(queue, (weight, parent, neighbour))
    cost = sum([w for _, _, w in mst])
    return mst, cost


def replaceCharByIndex(graph):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for edges in graph:
        for edge in edges:
            edge[0] = characters.index(edge[0])
            edge[2] = characters.index(edge[2])
    return graph


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
# print(primMST(tupleList, 0))

test = {
    "0": {"1": 9, "2": 5, "3": 2},
    "1": {"0": 9, "3": 6, "4": 5},
    "2": {"0": 5, "3": 4, "4": 5},
    "3": {"0": 2, "1": 6, "2": 4, "4": 4},
    "4": {"1": 5, "2": 5, "3": 4},
}

# xx = adjacencyListToTuplesList(test)
# xxx = primTupleList(xx)
# print(xxx)
# print(primMST(xxx, 0))

# parent, weight, node
g = [
    [["A", 4, "B"], ["A", 2, "D"]],
    [["B", 4, "A"], ["B", 4, "C"], ["B", 6, "E"]],
    [["C", 4, "B"], ["C", 7, "E"]],
    [["D", 2, "A"], ["D", 3, "E"], ["D", 5, "F"]],
    [["E", 6, "B"], ["E", 7, "C"], ["E", 3, "D"], ["E", 8, "H"]],
    [["F", 5, "D"], ["F", 9, "G"]],
    [["G", 9, "F"], ["G", 3, "H"]],
    [["H", 8, "E"], ["H", 3, "G"]],
]
g = replaceCharByIndex(g)
mst, cost = primMST(g, 0, isMax=True)
mst = [(chr(parent + 65), chr(node + 65), weight) for parent, node, weight in mst]
print(mst, cost)

# parent, weight, node
g = [
    [
        [0, 240, 2 - 1],
        [0, 210, 3 - 1],
        [0, 340, 4 - 1],
        [0, 280, 5 - 1],
        [0, 200, 6 - 1],
        [0, 345, 7 - 1],
        [0, 120, 8 - 1],
    ],
    [
        [1, 240, 1 - 1],
        [1, 265, 3 - 1],
        [1, 175, 4 - 1],
        [1, 215, 5 - 1],
        [1, 180, 6 - 1],
        [1, 185, 7 - 1],
        [1, 155, 8 - 1],
    ],
    [
        [2, 210, 1 - 1],
        [2, 265, 2 - 1],
        [2, 260, 4 - 1],
        [2, 115, 5 - 1],
        [2, 350, 6 - 1],
        [2, 435, 7 - 1],
        [2, 195, 8 - 1],
    ],
    [
        [3, 340, 1 - 1],
        [3, 175, 2 - 1],
        [3, 260, 3 - 1],
        [3, 160, 5 - 1],
        [3, 330, 6 - 1],
        [3, 295, 7 - 1],
        [3, 230, 8 - 1],
    ],
    [
        [4, 280, 1 - 1],
        [4, 215, 2 - 1],
        [4, 115, 3 - 1],
        [4, 160, 4 - 1],
        [4, 360, 6 - 1],
        [4, 400, 7 - 1],
        [4, 170, 8 - 1],
    ],
    [
        [5, 200, 1 - 1],
        [5, 180, 2 - 1],
        [5, 350, 3 - 1],
        [5, 330, 4 - 1],
        [5, 360, 5 - 1],
        [5, 175, 7 - 1],
        [5, 205, 8 - 1],
    ],
    [
        [6, 345, 1 - 1],
        [6, 185, 2 - 1],
        [6, 435, 3 - 1],
        [6, 295, 4 - 1],
        [6, 400, 5 - 1],
        [6, 175, 6 - 1],
        [6, 305, 8 - 1],
    ],
    [
        [7, 120, 1 - 1],
        [7, 155, 2 - 1],
        [7, 195, 3 - 1],
        [7, 230, 4 - 1],
        [7, 170, 5 - 1],
        [7, 205, 6 - 1],
        [7, 305, 7 - 1],
    ],
]
# mst, cost = primMST(g, 0)
# print(mst, cost)
