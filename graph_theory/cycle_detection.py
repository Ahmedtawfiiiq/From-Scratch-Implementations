def isCyclic(graph):
    visited = set()
    recursionStack = set()
    for node in graph:
        if node not in visited:
            if cycleDetection_dfs(graph, node, visited, recursionStack):
                return True  # cycle exists
    return False  # no cycle exists


def cycleDetection_dfs(graph, node, visited, recursionStack):
    visited.add(node)
    recursionStack.add(node)
    for neighbour in graph[node]:
        if neighbour not in visited:
            if cycleDetection_dfs(graph, neighbour, visited, recursionStack):
                return True
        # if neighbour is visited and in recursionStack, then cycle exists
        elif neighbour in recursionStack:
            return True
    recursionStack.remove(node)
    return False


g = {
    "1": ["2"],
    "2": ["3"],
    "3": ["4", "7"],
    "4": ["5"],
    "5": ["6"],
    "6": [],
    "7": ["5"],
    "8": ["9"],
    "9": ["10"],
    "10": ["8"],
}

print(isCyclic(g))
