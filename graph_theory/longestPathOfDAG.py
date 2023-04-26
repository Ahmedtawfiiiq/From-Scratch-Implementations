from topologicalSort import topologicalSortDFS
from general import reconstructPath


# on a directed acyclic graph
def singleSourceShortestPath(weightedGraph, source):
    ordering = topologicalSortDFS(weightedGraph)
    distances = {}
    for node in weightedGraph:
        distances[node] = float("inf")
    distances[source] = 0
    parent = {}
    for node in ordering:
        for neighbour in weightedGraph[node]:
            # newDistance is current distance to src + weight of edge from src to dest
            # distances[neighbour] is the current distance to dest
            newDistance = distances[node] + weightedGraph[node][neighbour]
            if distances[neighbour] > newDistance:
                distances[neighbour] = newDistance
                parent[neighbour] = node
    return parent, distances


g = {
    "0": {"1": 2},
    "1": {"3": 1},
    "2": {"3": 3},
    "3": {},
    "4": {"0": 3, "2": 1},
    "5": {"4": 1},
    "6": {"4": 2, "5": 3},
}
p, dist = singleSourceShortestPath(g, "6")
print(dist)
# sorted_dist = dict(sorted(dist.items()))
print(dist.values())


# # on a directed acyclic graph
# def longestPath(weightedGraph, source):
#     # step 1: topological sort
#     orderings = topologicalSortDFS(weightedGraph)
#     # longest path trick - negate the weights
#     for node in weightedGraph:
#         for neighbour in weightedGraph[node]:
#             weightedGraph[node][neighbour] = -weightedGraph[node][neighbour]
#     # step 2: single source shortest path
#     distances = singleSourceShortestPath(weightedGraph, orderings)
#     for key in distances:
#         distances[key] = -distances[key]
#     return distances

# print(singleSourceShortestPath(weightedGraph, topologicalSortDFS(weightedGraph)))
# print(longestPath(dag))
