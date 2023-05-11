from collections import defaultdict


def dfsRecursive(graph, start, arrangement):
    while graph[start]:
        next_node = graph[start].pop()
        dfsRecursive(graph, next_node, arrangement)
        arrangement.append([start, next_node])


def eulerianPath(pairs):
    start = pairs[0][0]  # assume eulerian circuit
    graph = defaultdict(list)
    count = defaultdict(int)
    for pair in pairs:
        graph[pair[0]].append(pair[1])
        count[pair[0]] += 1
        count[pair[1]] -= 1
    for key in count:  # eulerian path check
        if count[key] == 1:
            start = key
            break
    arrangement = []
    dfsRecursive(graph, start, arrangement)
    return arrangement[::-1]


edgeList = [
    [1, 2],
    [1, 3],
    [2, 2],
    [2, 4],
    [2, 4],
    [3, 1],
    [3, 2],
    [3, 5],
    [4, 3],
    [4, 6],
    [5, 6],
    [6, 3],
]
print(eulerianPath(edgeList))
