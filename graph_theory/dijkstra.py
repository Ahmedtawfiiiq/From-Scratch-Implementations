from general import reconstructPath


# single source shortest path algorithm
def dijkstra(graph, start, end):
    visited = set()
    path = {}
    distances = {}
    prioriyQueue = {}
    for node in graph:
        distances[node] = float("inf")
    distances[start] = 0
    prioriyQueue[start] = distances[start]
    while prioriyQueue:
        prioriyQueue = dict(sorted(prioriyQueue.items(), key=lambda item: item[1]))
        node = next(iter(prioriyQueue))
        prioriyQueue.pop(node)
        visited.add(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                newDistance = distances[node] + graph[node][neighbour]
                if newDistance < distances[neighbour]:
                    distances[neighbour] = newDistance
                    prioriyQueue[neighbour] = distances[neighbour]
                    path[neighbour] = node
        if node == end:
            # stop early after updating nodes connected to end
            # optional: stop early before updating nodes connected to end
            break
    return distances, reconstructPath(path, start, end)


weightedGraph = {
    "S": {"T": 10, "Y": 5},
    "T": {"X": 1, "Y": 2},
    "X": {"Z": 4},
    "Y": {"T": 3, "X": 9, "Z": 2},
    "Z": {"S": 7, "X": 6},
}
print(dijkstra(weightedGraph, "S", "Z"))
