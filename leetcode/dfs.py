def dfs(root, target):
    if root is None:
        return None
    if root.val == target:
        return root
    
    left = dfs(root.left, target)
    if left is not None:
        return left
    
    return dfs(root.right, target)


def findVal(root, target_val):
    if root is None:
        return None
    if root.val == target_val:
        return root
    
    return findVal(root.left, target_val) or findVal(root.right, target_val)


"""
dfs template(root, state):
    if root is None:
        ......
    return

    left = dfs template(root.left, state)
    right = dfs template(root.right, state)

    return 

"""