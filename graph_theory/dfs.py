from Ageneral import reconstructPath


def dfs(graph, node, visited=set(), order=[]):
    order.append(node)
    visited.add(node)
    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited, order)
    return order


def dfs_edge_list(graph, node, visited=set(), order=[]):
    order.append(node)
    visited.add(node)
    for edge in graph:
        if edge[0] == node and edge[1] not in visited:
            dfs_edge_list(graph, edge[1], visited, order)
    return order


def dfs_stack(g, src, end=None):
    order = []
    # parentMap = {}
    visited = set()
    stack = [src]
    visited.add(src)
    while stack:
        node = stack.pop(-1)  # first out
        order.append(node)
        # if node == end:
        # break
        children = g[node]
        for child in children:
            if child not in visited:
                stack.append(child)  # last in
                visited.add(child)
                # parentMap[child] = node
    return order
    # return reconstructPath(parentMap, src, end)


# function to find all paths between two nodes in a graph
# may be useful (not used yet)
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


# g = {"5": ["3", "7"], "3": ["2", "4"], "7": ["8"], "2": [], "4": ["8"], "8": []}
# print(findPaths(g, "5", "8"))


def sortGraph(graph, reverse=False):
    for node in graph:
        graph[node] = sorted(graph[node], reverse=reverse)
    return graph


g = {
    "A": ["B", "D"],
    "B": ["C", "E", "A"],
    "C": ["B", "E"],
    "D": ["A", "E", "F"],
    "E": ["B", "C", "D", "H"],
    "F": ["D", "G"],
    "G": ["F", "H"],
    "H": ["E", "G"],
}
print(dfs_stack(sortGraph(g, 1), "A"))
