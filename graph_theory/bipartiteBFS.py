from collections import defaultdict


def bfs(graph, start):
    order = []
    queue = [start]
    visited = set(start)
    while queue:
        parent = queue.pop(0)  # first out
        order.append(parent)
        for child in graph[parent]:
            if child not in visited:
                visited.add(child)
                queue.append(child)  # first in
    return order


# check is a given graph is bipartite or not using BFS
def isBipartiteBFS(graph, src):
    # 0: not colored, 1: blue, -1: red
    color = defaultdict(int)
    queue = [src]
    color[src] = 1  # blue
    while queue:
        parent = queue.pop(0)
        for child in graph[parent]:
            if not color[child]:
                color[child] = -color[parent]
                queue.append(child)
            elif color[child] == color[parent]:
                return False
    return True


g = {
    "a": ["e"],
    "b": ["e"],
    "c": ["e"],
    "d": ["e"],
    "e": ["a", "b", "c", "d"],
}
print(isBipartiteBFS(g, "a"))
