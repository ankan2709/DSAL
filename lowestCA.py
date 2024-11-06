def lca(root, p, q):
    if root == None:
        return None
    
    if p < root and q < root:
        return lca(root.left, p, q)

    elif p > root and q > root:
        return lca(root.right, p, q)

    else:
        return root.val
