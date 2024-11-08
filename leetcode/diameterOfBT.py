res = [0]

def dfs(root):
    if not root:
        return None
    
    left = dfs(root.left)
    right = dfs(root.right)

    length = left + right
    res[0] = max(res[0], length)

    return 1 + max(left, right)

dfs(root)
print(res[0])