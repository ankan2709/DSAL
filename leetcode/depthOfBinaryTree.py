def dfs(root):
    if not root:
        return 0
    
    left = dfs(root.left)
    right = dfs(root.right)

    return 1 + max(left, right)