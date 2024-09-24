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


# g = {
#     "A": ["B", "C"],
#     "B": ["C", "F"],
#     "C": ["D"],
#     "D": [],
#     "E": [],
#     "F": ["D", "E"],
#     "G": ["B", "F"],
# }

# g = {
#     "0": [],
#     "1": [],
#     "2": ["3"],
#     "3": ["1"],
#     "4": ["0", "1"],
#     "5": ["0", "2"],
# }

# g = {
#     "0": {"1": 2},
#     "1": {"3": 1},
#     "2": {"3": 3},
#     "3": {},
#     "4": {"0": 3, "2": 1},
#     "5": {"4": 1},
#     "6": {"4": 2, "5": 3},
# }

g = {
    10: [9],
    1: [3],
    2: [1],
    3: [],
    4: [2, 3],
    5: [4],
    6: [9],
    7: [4],
    8: [5, 7],
    9: [5, 8],
}

print(topologicalSortDFS(g))
