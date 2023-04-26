def dfs(graph, node, visited=set(), order=[]):
    order.append(node)
    visited.add(node)
    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited, order)
    return order


g = {"5": ["3", "7"], "3": ["2", "4"], "7": ["8"], "2": [], "4": ["8"], "8": []}
print(dfs(g, "5"))
