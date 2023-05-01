import numpy as np
from dfs import findPaths
from general import weightedAdjacencyMatrixToAdjacencyList


def toResidualGraph(graph):
    n = len(graph)
    residualMatrix = np.zeros((n, n)).astype(int)
    for node in graph:
        for neighbour in graph[node]:
            flow = graph[node][neighbour][0]
            capacity = graph[node][neighbour][1]
            forwardEdge = capacity - flow
            backwardEdge = flow
            residualMatrix[node][neighbour] = forwardEdge
            residualMatrix[neighbour][node] = backwardEdge
    return residualMatrix


def fordFulkerson(graph, src, dst):
    residualMatrix = toResidualGraph(graph)
    residualList = weightedAdjacencyMatrixToAdjacencyList(residualMatrix)
    paths = findPaths(residualList, str(src), str(dst))
    # print(paths)
    while paths:
        index = int(input())
        path = paths[index]
        # path = paths[0]
        pathFlow = np.inf
        for i in range(len(path) - 1):
            node = path[i]
            neighbour = path[i + 1]
            edgeFlow = residualMatrix[int(node)][int(neighbour)]
            pathFlow = min(pathFlow, edgeFlow)
        for i in range(len(path) - 1):
            node = path[i]
            neighbour = path[i + 1]
            # check direction of edge
            if int(neighbour) in graph[int(node)]:  # forward edge
                graph[int(node)][int(neighbour)][0] += pathFlow
            else:  # backward edge
                graph[int(neighbour)][int(node)][0] -= pathFlow
        residualMatrix = toResidualGraph(graph)
        residualList = weightedAdjacencyMatrixToAdjacencyList(residualMatrix)
        paths = findPaths(residualList, str(src), str(dst))
        # print(paths)
    maxFlow = 0
    for neighbour in graph[src]:
        maxFlow += graph[src][neighbour][0]
    return maxFlow


# g = {
#     0: {1: [0, 3], 2: [0, 2]},
#     1: {4: [0, 2]},
#     2: {1: [0, 3], 3: [0, 3]},
#     3: {4: [0, 3], 5: [0, 2]},
#     4: {2: [0, 1], 5: [0, 3]},
#     5: {},
# }

# g = {
#     0: {1: [0, 10], 3: [0, 10]},
#     1: {2: [0, 4], 3: [0, 2], 4: [0, 8]},
#     2: {5: [0, 10]},
#     3: {4: [0, 9]},
#     4: {2: [0, 6], 5: [0, 10]},
#     5: {},
# }

# g = {
#     0: {1: [0, 4], 2: [0, 3]},
#     1: {2: [0, 2], 3: [0, 1]},
#     2: {3: [0, 3]},
#     3: {},
# }

g = {
    0: {1: [0, 8], 4: [0, 3]},
    1: {2: [0, 9]},
    2: {5: [0, 2]},
    3: {5: [0, 5]},
    4: {2: [0, 7], 3: [0, 4]},
    5: {},
}


print("max-flow:", fordFulkerson(g, 0, len(g) - 1))
