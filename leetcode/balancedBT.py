def isBalanced(root):
    if not root:
        return True
    balanced = [True]
    def dfs(root):
        if root is None:
            return 0
        
        left = dfs(root.left)
        right = dfs(root.right)

        if abs(left - right) > 1:
            balanced[0] = False
            return 0
        
        return 1 + max(left, right)
    dfs(root)
    return balanced[0]



