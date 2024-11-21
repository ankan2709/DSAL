def maxDepthOfBinaryTree(root):

    def dfs(root):
        if root is None:
            return 0
        
        left = maxDepthOfBinaryTree(root.right)
        right = maxDepthOfBinaryTree(root.right)

        return 1 + max(left, right)
    return dfs(root) - 1 if root else 0


