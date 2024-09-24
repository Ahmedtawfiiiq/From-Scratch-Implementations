from topologicalSort import topologicalSortDFS


# dynamic programming
def dagSSSP(weightedGraph, source):
    ordering = topologicalSortDFS(weightedGraph)
    distances = {}
    for node in weightedGraph:
        distances[node] = float("inf")
    distances[source] = 0
    for node in ordering:
        for neighbour in weightedGraph[node]:
            # relax edge
            distances[neighbour] = min(
                distances[neighbour],  # current distance
                distances[node] + weightedGraph[node][neighbour],  # new distance
            )
    return distances


def recursive_dagSSSP(weightedGraph, source, distances=None):
    if distances is None:
        distances = {}
        for node in weightedGraph:
            distances[node] = float("inf")
        distances[source] = 0
    for neighbour in weightedGraph[source]:
        newDistance = distances[source] + weightedGraph[source][neighbour]
        if distances[neighbour] > newDistance:
            distances[neighbour] = newDistance
            recursive_dagSSSP(weightedGraph, neighbour, distances)
    return distances


g = {
    "0": {"1": 2},
    "1": {"3": 1},
    "2": {"3": 3},
    "3": {},
    "4": {"0": 3, "2": 1},
    "5": {"4": 1},
    "6": {"4": 2, "5": 3},
}
dist = dagSSSP(g, "6")
print(list(dist.values()))

# topOrder = topologicalSortDFS(g)
# print("topological order:", topOrder)
# src = topOrder[0]
# dist = recursive_dagSSSP(g, src)
# print(list(dist.values()))
