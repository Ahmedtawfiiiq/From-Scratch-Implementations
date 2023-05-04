# single source shortest path algorithm
def bellmanFord(graph, start, showImpactOfNegativeCycles=False):
    distances = {}
    path = {}
    for node in graph:
        distances[node] = float("inf")
    distances[start] = 0
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))
    # relax each edge V - 1 times ( V = number of nodes(vertices))
    for i in range(2):
        for _ in range(len(graph) - 1):  # O(V)
            for edge in edges:  # O(E)
                node = edge[0]  # parent (source)
                neighbour = edge[1]  # child (destination)
                newDistance = distances[node] + graph[node][neighbour]
                if newDistance < distances[neighbour]:
                    if i == 0:  # relaxation in first iteration
                        distances[neighbour] = newDistance
                        path[neighbour] = node
                    else:  # check for negative cycles in second iteration
                        if (
                            showImpactOfNegativeCycles
                        ):  # takes 2*(V - 1) iterations to get the impact of negative cycles
                            # if we obtained a better distance after V - 1 iterations
                            # nodes in negative cycle and nodes reachable by negative cycle have infinite distance (unreachable)
                            # there is no distinction between the type of the two nodes in this implementation
                            distances[neighbour] = -float("inf")
                        else:  # takes only V iterations to detect negative cycles
                            return "Negative cycle detected"
    return distances


weightedGraph = {
    "0": {"1": 5},
    "1": {"2": 20, "6": 60, "5": 30},
    "2": {"3": 10, "4": 75},
    "3": {"2": -15},
    "4": {"9": 100},
    "5": {"4": 25, "6": 5, "8": 50},
    "6": {"7": -50},
    "7": {"8": -10},
    "8": {},
    "9": {},
}

print(bellmanFord(weightedGraph, "0", showImpactOfNegativeCycles=False))
