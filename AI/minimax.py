# Minimax algorithm using alpha-beta pruning
def minimax(node, alpha, beta, maximizingPlayer):
    if len(node.children) == 0:
        return node.value

    if maximizingPlayer:
        value = -float("inf")
        for child in node.children:
            value = max(value, minimax(child, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value

    else:
        value = float("inf")
        for child in node.children:
            value = min(value, minimax(child, alpha, beta, True))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value


# define the class for the node
class Node:
    def __init__(self, value, children):
        self.value = value
        self.children = children


# assume perfect binary tree
def minimaxTree(l, internalLevels):
    leaves = [Node(i, []) for i in l]
    nodes = [[] for _ in range(internalLevels)]
    nodes[0] = [Node(None, leaves[2 * i : 2 * i + 2]) for i in range(len(leaves) // 2)]
    for i in range(1, internalLevels):
        nodes[i] = [
            Node(None, nodes[i - 1][2 * j : 2 * j + 2])
            for j in range(len(nodes[i - 1]) // 2)
        ]
    root = Node(None, nodes[-1])
    return root


l = [10, 5, 7, 11, 12, 8, 9, 8, 5, 12, 11, 12, 9, 8, 7, 10]
internalLevels = 3
root = minimaxTree(l, internalLevels)
alpha = -float("inf")
beta = float("inf")

# root is maximizing player
player = True
print(minimax(root, alpha, beta, player))
