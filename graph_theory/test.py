# find neighbours of a node in a grid
def findNeighbours(graph, node):
    dr = [1, 1, 1]
    dc = [-1, 0, 1]
    neighbours = []
    for i in range(len(dr)):
        r = node[0] + dr[i]
        c = node[1] + dc[i]
        if r >= 0 and r < len(graph) and c >= 0 and c < len(graph[0]):
            neighbours.append((r, c))
    return neighbours


# reconstruct shortest path from start to end
def reconstructPath(parentMap, start, end):
    path = []
    at = end  # assume end is connected to start
    while at is not None:
        path.append(at)
        at = parentMap.get(at)
    path.reverse()
    if path[0] == start:  # if start and end are connected
        return path
    # if start and end are not connected
    return []


def to_adjacency_list(matrix):
    g = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            g[(i, j)] = {}
            neighbours = findNeighbours(matrix, (i, j))
            for neighbour in neighbours:
                if neighbour not in g[(i, j)]:
                    g[(i, j)][neighbour] = matrix[neighbour[0]][neighbour[1]]
                else:
                    g[(i, j)][neighbour].update(matrix[neighbour[0]][neighbour[1]])
    return g


def dfs(graph, node, visited, stack):
    visited.add(node)
    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited, stack)
    stack.append(node)


# on a directed acyclic graph
def topologicalSortDFS(graph):
    stack = []
    visited = set()
    for node in graph:  # start dfs from every node
        if node not in visited:
            dfs(graph, node, visited, stack)
    orderings = []
    while stack:
        orderings.append(stack.pop())
    return orderings


# on a directed acyclic graph
def singleSourceShortestPath(weightedGraph, source, matrix):
    ordering = topologicalSortDFS(weightedGraph)
    while ordering[0] != source:
        ordering.pop(0)
    distances = {}
    for node in weightedGraph:
        distances[node] = float("inf")
    for node in weightedGraph:
        if node[0] == 0:
            distances[node] = matrix[node[0]][node[1]]
    parent = {}
    for node in ordering:
        for neighbour in weightedGraph[node]:
            # newDistance is current distance to src + weight of edge from src to dest
            # distances[neighbour] is the current distance to dest
            newDistance = distances[node] + weightedGraph[node][neighbour]
            if distances[neighbour] > newDistance:
                distances[neighbour] = newDistance
                parent[neighbour] = node
    return parent


def minimumFallingPathSum(matrix):
    g = to_adjacency_list(matrix)
    print(g)
    minimumSum = float("inf")
    for i in range(len(matrix[0])):
        parent = singleSourceShortestPath(g, (0, i), matrix)
        smallestEnd = float("inf")
        end = None
        for node in parent:
            if node[0] == len(matrix) - 1:
                if smallestEnd > matrix[node[0]][node[1]]:
                    end = node
                    smallestEnd = min(smallestEnd, matrix[node[0]][node[1]])
        path = reconstructPath(parent, (0, i), end)
        m = 0
        for node in path:
            m += matrix[node[0]][node[1]]
        minimumSum = min(minimumSum, m)
        # print(minimumSum)
    return minimumSum


import numpy as np


# dr = [1, 1, 1]
# dc = [-1, 0, 1]
# neighbours = []
# for i in range(len(dr)):
#     r = node[0] + dr[i]
#     c = node[1] + dc[i]
#     if r >= 0 and r < len(graph) and c >= 0 and c < len(graph[0]):
#         neighbours.append((r, c))
# return neighbours
def fun(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    minSum = np.array(matrix)
    for i in range(1, len(matrix)):
        for j in range(len(matrix[0])):
            if j == 0:
                minSum[i][j] = (
                    min(minSum[i - 1][j], minSum[i - 1][j + 1]) + matrix[i][j]
                )
            elif j == len(matrix[0]) - 1:
                minSum[i][j] = (
                    min(minSum[i - 1][j], minSum[i - 1][j - 1]) + matrix[i][j]
                )
            else:
                minSum[i][j] = (
                    min(minSum[i - 1][j - 1], minSum[i - 1][j], minSum[i - 1][j + 1])
                    + matrix[i][j]
                )
    return min(minSum[-1])


matrix = [[17, 82], [1, -44]]
# matrix = [[-19, 57], [-40, -5]]
# print(minimumFallingPathSum(matrix))
print(fun(matrix))
