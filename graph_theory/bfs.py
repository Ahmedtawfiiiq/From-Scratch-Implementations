from Ageneral import reconstructPath, findNeighbours


# find shortest path from start to end
def bfs(graph, start, end=None, filter=None):
    order = []
    # parentMap = {}
    visited = set()
    queue = [start]
    visited.add(start)
    while queue:
        parent = queue.pop(0)  # first out
        order.append(parent)
        # if parent == end:
            # break
        children = graph[parent]  # find neighbours if adjacency list
        # children = findNeighbours(graph, parent, filter)  # find neighbours if grid
        for child in children:
            if child not in visited:
                queue.append(child)  # first in
                visited.add(child)
                # parentMap[child] = parent
    # print()
    return order
    # return reconstructPath(parentMap, start, end)


# g = {"5": ["3", "7"], "3": ["2", "4"], "7": ["8"], "2": [], "4": ["8"], "8": []}
# print(bfs(g, "5", "8"))

# grid
# dungeon = [
#     ["S", ".", ".", "#", ".", ".", "."],
#     [".", "#", ".", ".", ".", "#", "."],
#     [".", "#", ".", ".", ".", ".", "."],
#     [".", ".", "#", "#", ".", ".", "."],
#     ["#", ".", "#", "E", ".", "#", "."],
# ]
# start = (0, 0), end = (4, 3)
# order, path = bfs(dungeon, (0, 0), (4, 3), filter="#")
# print(path)

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
print(bfs(sortGraph(g, 0), "A"))

