def findNeighbours(graph, node):
    # north, south, east, west
    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]
    neighbours = []
    for i in range(4):
        r = node[0] + dr[i]
        c = node[1] + dc[i]
        if (
            r >= 0
            and r < len(graph)
            and c >= 0
            and c < len(graph[0])
            and graph[node[0]][node[1]] == graph[r][c]
        ):
            neighbours.append((r, c))
    return neighbours


def dfs(grid, node, color, visited):
    visited.add(node)
    neighbours = findNeighbours(grid, node)
    grid[node[0]][node[1]] = color
    for neighbour in neighbours:
        if neighbour not in visited:
            dfs(grid, neighbour, color, visited)


image = [[0, 0, 0], [0, 0, 0]]
sr = 1
sc = 1
color = 2
dfs(image, (sr, sc), color, set())
print(image)


# result
x = [
    [2, 2, 2],
    [2, 2, 0],
    [2, 0, 1],
]
