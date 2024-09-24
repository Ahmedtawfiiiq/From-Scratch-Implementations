def hierholzer(graph, start, type="undirected"):
    # assume eulerian cycle: all vertices have even degree
    cpath = []
    epath = []
    cpath.append(start)
    while cpath:
        node = cpath[-1]  # top of cpath stack
        if graph[node] == []:
            epath.append(cpath.pop())
        else:
            next_node = graph[node][-1]  # last node is selected first
            cpath.append(next_node)
            # delete edge
            if type == "undirected":
                graph[node].remove(next_node)
                graph[next_node].remove(node)
            else:
                graph[node].remove(next_node)
    return epath[::-1]


undirectedGraph = {
    1: [2, 6],
    2: [1, 3, 4, 5],
    3: [2, 6],
    4: [2, 5],
    5: [2, 4],
    6: [1, 3],
}

directedGraph = {
    1: [10],
    2: [1, 6],
    3: [11],
    4: [3, 5],
    5: [2, 10],
    6: [9],
    7: [8],
    8: [4, 5],
    9: [2],
    10: [8, 7],
    11: [4],
}

start_node = 1
# print(hierholzer(undirectedGraph, start_node, type="undirected"))
print(hierholzer(directedGraph, start_node, type="directed"))
