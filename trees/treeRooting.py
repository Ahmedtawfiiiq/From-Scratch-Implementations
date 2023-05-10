# convert an undirected tree to a directed tree
# def rooting(t, root, visited, rooted_tree):
#     visited.add(root)
#     for neighbor in t[root]:
#         if neighbor not in visited:
#             node = rooting(t, neighbor, visited, rooted_tree)
#             if root not in rooted_tree:
#                 rooted_tree[root] = [node]
#             else:
#                 rooted_tree[root].append(node)
#     for node in t:
#         if node not in rooted_tree:
#             rooted_tree[node] = []
#     return root


# rooting a tree using DFS
def rootTree(t, root):
    visited = set()
    rooted_tree = {}
    rooted_tree[root] = []
    stack = [root]
    while stack:
        node = stack.pop()
        visited.add(node)
        for neighbor in t[node]:
            if neighbor not in visited:
                stack.append(neighbor)
                if node not in rooted_tree:
                    rooted_tree[node] = [neighbor]
                else:
                    rooted_tree[node].append(neighbor)
    for node in t:
        if node not in rooted_tree:
            rooted_tree[node] = []
    return rooted_tree


tree = {
    0: [2, 1, 5],
    1: [0],
    2: [3, 0],
    3: [2],
    4: [5],
    5: [4, 6, 0],
    6: [5],
}


rooted_tree = rootTree(tree, 0)
print(rooted_tree)
