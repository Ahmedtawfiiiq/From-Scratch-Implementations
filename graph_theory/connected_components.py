from general import graphMatrixToAdjacencyList, directed_to_undirected


def dfs(graph, node, visited, connectedComponents=1, components=None):
    visited.add(node)
    components[node] = connectedComponents
    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited, connectedComponents, components)


# assume the graph to be undirected
def findConnectedComponentsDFS(graph):
    components = {}
    visited = set()
    connectedComponents = 0
    for node in graph:
        if node not in visited:
            connectedComponents += 1
            dfs(graph, node, visited, connectedComponents, components)
    return connectedComponents, components


# directed graph
g = {
    "0": ["8"],
    "1": ["5"],
    "2": ["9"],
    "3": ["9"],
    "4": ["0"],
    "5": ["16", "17"],
    "6": ["11"],
    "7": ["6"],
    "8": ["4", "14"],
    "9": ["15"],
    "10": [],
    "11": ["7"],
    "12": [],
    "13": ["0"],
    "14": ["0", "13"],
    "15": ["2", "10"],
    "16": [],
    "17": [],
}

cities = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
g = graphMatrixToAdjacencyList(cities)
undirected_graph = directed_to_undirected(g)
numberOfComponents, labeledNodes = findConnectedComponentsDFS(undirected_graph)
# for i in range(1, numberOfComponents + 1):
#     for key in labeledNodes:
#         if labeledNodes[key] == i:
#             print(key, end=" ")
#     print("Done")
print(numberOfComponents)
