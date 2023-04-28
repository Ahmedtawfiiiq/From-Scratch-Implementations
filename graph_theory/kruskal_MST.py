from union_find import UnionFind


def kruskal_MST(g):
    edges = []
    for u in g:
        for v in g[u]:
            edges.append((g[u][v], u, v))  # (weight, src, dst)
    edges.sort()
    mst = []
    uf = UnionFind(len(g))
    for w, u, v in edges:
        if not uf.connected(u, v):
            uf.unify(u, v)
            mst.append((u, v, w))
    cost = sum([w for _, _, w in mst])
    return mst, cost


# keys are integers, values are dictionaries
g = {
    "0": {"1": 9, "2": 5, "3": 2},
    "1": {"0": 9, "3": 6, "4": 5},
    "2": {"0": 5, "3": 4, "4": 5},
    "3": {"0": 2, "1": 6, "2": 4, "4": 4},
    "4": {"1": 5, "2": 5, "3": 4},
}

print(kruskal_MST(g))
