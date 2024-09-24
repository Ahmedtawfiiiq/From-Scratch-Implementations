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


# find neighbours of a node in a grid
def findNeighbours(graph, node, filter=None):
    # north, south, east, west
    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]
    neighbours = []
    for i in range(4):
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


def directed_to_undirected(graph):
    # if there is an edge from a to b, add an edge from b to a
    for node in graph:
        for neighbour in graph[node]:
            if node not in graph[neighbour]:
                graph[neighbour].append(node)
    return graph


# for unwieghted graphs
def adjacencyMatrixToAdjacencyList(adjacencyMatrix):
    g = {}
    for i in range(len(adjacencyMatrix)):
        g[str(i)] = []
        for j in range(len(adjacencyMatrix[0])):
            if adjacencyMatrix[i][j] == 1:
                g[str(i)].append(str(j))
    return g


# for unwieghted graphs
def adjacencyListToAdjacencyMatrix(adjacencyList):
    n = len(adjacencyList)
    adjacencyMatrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in adjacencyList[str(i)]:
            adjacencyMatrix[i][int(j)] = 1
    return adjacencyMatrix


# for weighted graphs
def weightedAdjacencyListToAdjacencyMatrix(adjacencyList):
    n = len(adjacencyList)
    adjacencyMatrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        node = str(i)
        for neighbour in adjacencyList[node]:
            if adjacencyList[node][neighbour] == 0:
                adjacencyMatrix[i][int(neighbour)] = 0.1
            else:
                adjacencyMatrix[i][int(neighbour)] = adjacencyList[node][neighbour]
    return adjacencyMatrix


# for weighted graphs
def weightedAdjacencyMatrixToAdjacencyList(adjacencyMatrix):
    n = len(adjacencyMatrix)
    adjacencyList = {}
    for i in range(n):
        adjacencyList[str(i)] = {}
        for j in range(n):
            if adjacencyMatrix[i][j] != 0:
                adjacencyList[str(i)][str(j)] = adjacencyMatrix[i][j]
    return adjacencyList


# function to convert adjacency list to list of edges
# where each edge is represented by a tuple (destination ,weight)
def adjacencyListToTuplesList(adjacencyList):
    edges = [[] for _ in range(len(adjacencyList))]
    for node in adjacencyList:
        for neighbour in adjacencyList[node]:
            edges[int(node)].append((int(neighbour), adjacencyList[node][neighbour]))
    return edges


# import os
# os.environ['PYTHONHASHSEED'] = '0'


# adjacency list
# g = {"5": ["3", "7"], "3": ["2", "4"], "7": [], "2": [], "4": [], "8": []} # two connected components
# g = {
#     "0": ["1", "2", "4"],
#     "1": ["0", "4"],
#     "2": ["0", "4", "5", "9", "10"],
#     "4": ["0", "1", "2"],
#     "5": ["2", "6", "7", "8"],
#     "6": ["5"],
#     "7": ["5", "8"],
#     "8": ["5", "7"],
#     "9": ["2", "11"],
#     "10": ["2", "11"],
#     "11": ["9", "10"],
# }


# weightedGraph = {
#     "A": {"B": 3, "C": 6},
#     "B": {"C": 4, "D": 4, "E": 11},
#     "C": {"D": 8, "G": 11},
#     "D": {"E": -4, "F": 5, "G": 2},
#     "E": {"H": 9},
#     "F": {"H": 1},
#     "G": {"H": 2},
#     "H": {},
# }

# weightedGraph = {
#     "0": {"1": 4, "2": 1},
#     "1": {"3": 1},
#     "2": {"1": 2, "3": 5},
#     "3": {"4": 3},
#     "4": {},
# }


# longestIncreasingSubsequence
# directed acyclic graph
# dag = {
#     "3": {"8": 1, "5": 1},
#     "1": {"8": 1, "2": 1, "5": 1},
#     "8": {},
#     "2": {"5": 1},
#     "5": {},
# }


# longest increasing subsequence is the longest path in a DAG + 1
# print(max(longestPath(dag).values()) + 1)
