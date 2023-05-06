from graph_theory.Ageneral import reconstructPath, findNeighbours


# find shortest path from start to end
def bfs(graph, start, end, filter=None):
    order = []
    parentMap = {}
    visited = set()
    queue = [start]
    visited.add(start)
    while queue:
        parent = queue.pop(0)  # first out
        order.append(parent)
        if parent == end:
            break
        children = graph[parent]  # find neighbours if adjacency list
        # children = findNeighbours(graph, parent, filter)  # find neighbours if grid
        for child in children:
            if child not in visited:
                queue.append(child)  # first in
                visited.add(child)
                parentMap[child] = parent
    # print()
    # return order
    return reconstructPath(parentMap, start, end)


g = {"5": ["3", "7"], "3": ["2", "4"], "7": ["8"], "2": [], "4": ["8"], "8": []}
# print(bfs(g, "5", "8"))

# grid
dungeon = [
    ["S", ".", ".", "#", ".", ".", "."],
    [".", "#", ".", ".", ".", "#", "."],
    [".", "#", ".", ".", ".", ".", "."],
    [".", ".", "#", "#", ".", ".", "."],
    ["#", ".", "#", "E", ".", "#", "."],
]  # start = (0, 0), end = (4, 3)
# order, path = bfs(dungeon, (0, 0), (4, 3), filter="#")
# print(path)
