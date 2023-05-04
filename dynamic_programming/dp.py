# convert an integer sequence to a directed acyclic graph
# to find the longest increasing subsequence
def sequence_to_dag(l):
    g = {}
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[j] > l[i]:
                neighbour = {}
                neighbour[l[j]] = 1
                # add neighbour as a new edge to the node i
                if l[i] in g:
                    g[l[i]].update(neighbour)
                else:
                    g[l[i]] = neighbour
        # if node i has no neighbours, add it to the graph
        if l[i] not in g:
            g[l[i]] = {}
    return g


def longestIncreasingSubsequence(l):
    table = [1] * len(l)
    prev = [None] * len(l)
    for i in range(1, len(l)):
        for j in range(i):
            if l[j] < l[i] and table[j] + 1 > table[i]:
                table[i] = table[j] + 1
                prev[i] = j
    max_index = table.index(max(table))
    lis = []
    while max_index is not None:
        lis.append(l[max_index])
        max_index = prev[max_index]
    lis.reverse()
    return lis, max(table)
    # table = [1] * len(l)
    # for i in range(1, len(l)):
    #     subproblems = [table[k] for k in range(i) if l[k] < l[i]]
    #     table[i] = max(subproblems, default=0) + 1  # if subproblems is empty, return 0
    # return max(table, default=0)  # if table is empty, return 0


# assume that the boxes cannot be rotated at any point during the process of stacking
def boxStacking(boxes):
    boxes = sorted(boxes)
    table = [0] * len(boxes)
    for i in range(len(boxes)):
        table[i] = boxes[i][2]
    for j in range(1, len(boxes)):
        maximum = 0
        for i in range(j):
            if boxes[i][0] < boxes[j][0] and boxes[i][1] < boxes[j][1]:
                if table[i] > maximum:
                    maximum = table[i]
        table[j] = maximum + table[j]
    return table[-1]


def numberOfWeakCharacters(properties):
    n = len(properties)
    properties = sorted(properties, reverse=True)
    table = [0] * n
    for j in range(1, n):
        for i in range(j):
            if (
                properties[i][0] > properties[j][0]
                and properties[i][1] > properties[j][1]
            ):
                table[j] = 1
                break
    return sum(table)


# table = [1 if properties[i][0] > properties[j][0] and properties[i][1] > properties[j][1] else 0 for i in range(n-1, -1, -1) for j in range(n-2, -1, -1)]


def boxes_to_dag(boxes):
    g = {}
    for i in range(len(boxes)):
        for j in range(len(boxes)):
            if boxes[i][0] < boxes[j][0] and boxes[i][1] < boxes[j][1]:
                edge = {}
                edge[boxes[j]] = boxes[j][2]
                if boxes[i] in g:
                    g[boxes[i]].update(edge)
                else:
                    g[boxes[i]] = edge
    return g


l = [3, 1, 8, 2, 5]
# find the longest increasing subsequence
# print(length_of_lis(l))

# print(longestIncreasingSubsequence(l))


# boxes = [(2, 3, 3), (2, 2, 4), (4, 4, 2)]
boxes = [(4, 5, 3), (2, 3, 2), (3, 6, 2), (1, 5, 4), (2, 4, 1), (1, 2, 2)]
# print(boxes)
print(boxStacking(boxes))
# print(boxes_to_dag(boxes))

# players = [[1, 5], [10, 4], [4, 3]]
# print(numberOfWeakCharacters(players))
