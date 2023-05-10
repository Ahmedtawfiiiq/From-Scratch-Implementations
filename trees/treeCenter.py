def findingTreeCenter(tree):
    while len(tree) > 2:
        leaves = []
        for node in tree:
            if len(tree[node]) == 1:
                leaves.append(node)
        for leaf in leaves:
            # each leaf has only one neighbor
            neighbor = tree[leaf][0]
            tree[neighbor].remove(leaf)
            del tree[leaf]
    return list(tree.keys())


t1 = {
    0: [1],
    1: [0, 2],
    2: [1, 3, 6, 9],
    3: [2, 4, 5],
    4: [3],
    5: [3],
    6: [2, 7, 8],
    7: [6],
    8: [6],
    9: [2],
}

t2 = {
    0: [1],
    1: [0, 3, 4],
    2: [3],
    3: [1, 2, 6, 7],
    4: [1, 5, 8],
    5: [4],
    6: [3, 9],
    7: [3],
    8: [4],
    9: [6],
}

print("tree 1 centers:", findingTreeCenter(t1))
print("tree 2 centers:", findingTreeCenter(t2))
