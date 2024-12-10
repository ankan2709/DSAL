def lowestCommonAncestor(root, p, q):
    if not root:
        return None

    if p < root.val and q < root.val:
        return lowestCommonAncestor(root.left, p, q)
    elif p > root.val and q > root.val:
        return lowestCommonAncestor(root.right, p, q)

    else:
        return root.val