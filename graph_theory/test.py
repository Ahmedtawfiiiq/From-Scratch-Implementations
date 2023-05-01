import numpy as np


def findNeighbours(graph, node, filter=None):
    dr = [-1, 1, 1, 1]
    dc = [0, -1, 0, 1]
    neighbours = []
    for i in range(len(dr)):
        r = node[0] + dr[i]
        c = node[1] + dc[i]
        if r >= 0 and r < len(graph) and c >= 0 and c < len(graph[0]):
            neighbours.append((r, c))
    n_neighbours = len(neighbours)
    for i in range(n_neighbours):
        for neighbour in neighbours:
            if graph[neighbour[0]][neighbour[1]] == filter:
                neighbours.remove(neighbour)
    return neighbours


def weightedAdjacencyMatrixToAdjacencyList(adjacencyMatrix):
    n = len(adjacencyMatrix)
    adjacencyList = {}
    for i in range(n):
        adjacencyList[str(i)] = {}
        for j in range(n):
            if adjacencyMatrix[i][j] != 0:
                adjacencyList[str(i)][str(j)] = adjacencyMatrix[i][j]
    return adjacencyList


def findPaths(graph, src, dst, path=[]):
    path = path + [src]
    if src == dst:
        return [path]
    if src not in graph:
        return []
    paths = []
    for node in graph[src]:
        if node not in path:
            newpaths = findPaths(graph, node, dst, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def toResidualGraph(graph):
    residualList = {}
    for node in graph:
        residualList[node] = {}
        for neighbour in graph[node]:
            flow = graph[node][neighbour][0]
            capacity = graph[node][neighbour][1]
            forwardEdge = capacity - flow
            backwardEdge = flow
            if forwardEdge != 0:
                residualList[node][neighbour] = forwardEdge
            if backwardEdge != 0:
                residualList[neighbour][node] = backwardEdge
    return residualList


def fordFulkerson(graph, src, dst):
    residualList = toResidualGraph(graph)
    paths = findPaths(residualList, src, dst)
    # print(paths)
    while paths:
        # index = int(input())
        # path = paths[index]
        path = paths[0]
        pathFlow = np.inf
        for i in range(len(path) - 1):
            node = path[i]
            neighbour = path[i + 1]
            edgeFlow = residualList[int(node)][int(neighbour)]
            pathFlow = min(pathFlow, edgeFlow)
        for i in range(len(path) - 1):
            node = path[i]
            neighbour = path[i + 1]
            # check direction of edge
            if int(neighbour) in graph[int(node)]:  # forward edge
                graph[int(node)][int(neighbour)][0] += pathFlow
            else:  # backward edge
                graph[int(neighbour)][int(node)][0] -= pathFlow
        residualList = toResidualGraph(graph)
        paths = findPaths(residualList, str(src), str(dst))
        # print(paths)
    maxFlow = 0
    for neighbour in graph[src]:
        maxFlow += graph[src][neighbour][0]
    return maxFlow


def gridToGraph(grid):
    m = len(grid)
    n = len(grid[0])
    graph = {}
    for i in range(m):
        for j in range(n):
            if grid[i][j] == ".":
                graph[(i, j)] = {}
                neighbours = findNeighbours(grid, (i, j), "#")
                for neighbour in neighbours:
                    graph[(i, j)][neighbour] = [0, 1]
    return graph


seats = [
    ["#", ".", "#", "#", ".", "#"],
    [".", "#", "#", "#", "#", "."],
    ["#", ".", "#", "#", ".", "#"],
]
g = gridToGraph(seats)
# print(g)
# g = {
#     (0, 1): {},
#     (0, 4): {(1, 5): [0, 1]},
#     (1, 0): {(2, 1): [0, 1]},
#     (1, 5): {(0, 4): [0, 1]},
#     (2, 1): {(1, 0): [0, 1]},
#     (2, 4): {},
# }
# m = 3
# n = 6
# print(toResidualGraph(g, m, n))
keys = list(g.keys())
print("max-flow:", fordFulkerson(g, keys[0], keys[-1]))
