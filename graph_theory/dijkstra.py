from heapq import heappop, heappush


def dijkstra_matrix(g, source):
    queue = [(0, source)]
    cDist = {source: 0}
    visited = set()
    while queue:
        dist, node = heappop(queue)
        if node in visited:
            continue
        visited.add(node)
        for neighbour, weight in g[node]:
            if neighbour not in visited:
                if neighbour not in cDist or dist + weight < cDist[neighbour]:
                    heappush(queue, (dist + weight, neighbour))
                    cDist[neighbour] = dist + weight
    return cDist


def edgeListToAdjacencyList(edges, n):
    # labels the nodes from 0 to n-1
    # given that the nodes are labeled from 1 to n
    for edge in edges:
        edge[0] -= 1
        edge[1] -= 1
    # print(edges)
    g = [[] for _ in range(n)]
    for edge in edges:
        g[edge[0]].append((edge[1], edge[2]))
    return g


n = 3
times = [[1, 2, 1], [2, 3, 2], [1, 3, 1]]
g = edgeListToAdjacencyList(times, n)
print(g)
k = 2
source = k - 1
result = dijkstra_matrix(g, source)
