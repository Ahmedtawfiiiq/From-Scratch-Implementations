from nodeClass import TreeNode


def maxDepth(root):
    if not root:
        return 0
    leftHeight = maxDepth(root.left)
    rightHeight = maxDepth(root.right)
    return max(leftHeight, rightHeight) + 1


# function to check if a binary tree is balanced
def isBalanced(root):
    if not root:
        return True
    leftHeight = maxDepth(root.left)
    rightHeight = maxDepth(root.right)
    if abs(leftHeight - rightHeight) > 1:
        return False
    return isBalanced(root.left) and isBalanced(root.right)


a = TreeNode(1)
print(isBalanced(a))
