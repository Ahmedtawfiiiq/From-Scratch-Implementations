from inputFile import takeInput
from heapq import heappop, heappush
import networkx as nx
import matplotlib.pyplot as plt


# dijkstra's algorithm using networkx
def networkxDijkstra(graph, source):
    g = nx.Graph()
    for node in graph:
        g.add_node(node)
        for neighbour in graph[node]:
            g.add_edge(node, neighbour, weight=int(graph[node][neighbour]))
    paths = []
    for node in g:
        if node != source:
            paths.append(nx.dijkstra_path(g, source, node))
    table = {}
    for path in paths:
        table[path[-1]] = [path[0], path[1]]
    return table


def reconstructPath(parentMap, start, end):
    path = []
    at = end  # assume end is connected to start
    while at is not None:
        path.append(at)
        at = parentMap.get(at)
    path.reverse()
    if path[0] == start:  # if start and end are connected
        return path
    # if start and end are not connected
    return []


def dijkstra(g, source, destination):
    queue = [(0, source)]
    parentMap = {source: None}
    distances = {source: 0}
    visited = set()
    while queue:
        dist, node = heappop(queue)
        if node in visited:
            continue
        visited.add(node)
        for neighbour in g[node]:
            if neighbour not in visited:
                weight = int(g[node][neighbour])
                if neighbour not in distances or dist + weight < distances[neighbour]:
                    heappush(queue, (dist + weight, neighbour))
                    distances[neighbour] = dist + weight
                    parentMap[neighbour] = node
    return distances
    # path = reconstructPath(parentMap, source, destination)
    # return path


def forwardingTable(g, source):
    table = {}
    paths = []
    for node in g:
        if node != source:
            paths.append(dijkstra(g, source, node))
    for path in paths:
        table[path[-1]] = [path[0], path[1]]
    return table


def visualize(graph):
    g = nx.Graph()
    for node in graph:
        g.add_node(node)
        for neighbour in graph[node]:
            g.add_edge(node, neighbour, weight=graph[node][neighbour])
    pos = nx.circular_layout(g)
    nx.draw(g, pos, with_labels=True)
    labels = nx.get_edge_attributes(g, "weight")
    nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)
    # mirror the graph
    plt.gca().invert_xaxis()
    plt.show()


# graph = takeInput()
# print(graph)
# g = {
#     "u": {"v": "2", "w": "5", "x": "1"},
#     "x": {"v": "2", "w": "3", "y": "1"},
#     "v": {"w": "3"},
#     "w": {"y": "1", "z": "5"},
#     "y": {"z": "2"},
#     "z": {},
# }

g = {
    "z": {"y": "12", "x": "8"},
    "y": {"t": "7", "v": "8", "x": "6"},
    "x": {"z": "8", "y": "6", "w": "6", "v": "3"},
    "w": {"x": "6", "v": "4", "u": "3"},
    "v": {"y": "8", "x": "3", "w": "4", "u": "3", "t": "4"},
    "u": {"w": "3", "v": "3", "t": "2"},
    "t": {"u": "2", "v": "4", "y": "7"},
}
source = "x"
for node in g:
    if node != source:
        print(dijkstra(g, source, node))
# table = forwardingTable(g, source)
