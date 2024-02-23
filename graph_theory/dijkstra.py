from heapq import heappop, heappush


def dijkstra_matrix(g, source):
    cost = {source: [0, source]}
    visited = set()
    queue = [(0, source)]
    while queue:
        dist, node = heappop(queue)
        if node not in visited:
            visited.add(node)
            for neighbour, weight in g[node]:
                if neighbour not in visited:
                    if neighbour not in cost or dist + weight < cost[neighbour][0]:
                        heappush(queue, (dist + weight, neighbour))
                        cost[neighbour] = [dist + weight, node]
    return cost


# g = {
#     "H": [["A", 3], ["B", 2], ["C", 5]],
#     "A": [("H", 3), ["D", 3]],
#     "B": [("H", 2), ["D", 1], ["E", 6]],
#     "C": [("H", 5), ["E", 2]],
#     "D": [("A", 3), ["B", 1], ["F", 4]],
#     "E": [("B", 6), ["C", 2], ["F", 1], ["S", 4]],
#     "F": [("D", 4), ["E", 1], ["S", 2]],
#     "S": [("F", 2), ["E", 4]],
# }
# source = "H"
# result = dijkstra_matrix(g, source)
# print(result)

g = {
    "A": [("B", 2), ("C", 1)],
    "B": [("A", 2), ("D", 0.5)],
    "C": [("A", 1), ("D", 1)],
    "D": [("B", 0.5), ("C", 1)],
}

# for each weight replace it with the multiplicative inverse
for node in g:
    g[node] = [(neighbour, 1 / weight) for neighbour, weight in g[node]]

source = "A"
result = dijkstra_matrix(g, source)
print(result)
