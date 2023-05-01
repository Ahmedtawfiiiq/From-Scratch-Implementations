def dfs(graph, node, visited=set(), order=[]):
    order.append(node)
    visited.add(node)
    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited, order)
    return order


def dfs_stack(g, src):
    order = []
    visited = set()
    stack = [src]
    visited.add(src)
    while stack:
        node = stack.pop(-1)  # first out
        order.append(node)
        children = g[node]
        for child in children:
            if child not in visited:
                stack.append(child)  # last in
                visited.add(child)
    return order


# function to find all paths between two nodes in a graph
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


g = {"5": ["3", "7"], "3": ["2", "4"], "7": ["8"], "2": [], "4": ["8"], "8": []}
# print(findPaths(g, "5", "8"))
