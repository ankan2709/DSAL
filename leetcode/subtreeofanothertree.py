def sameTree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return sameTree(p.left, q.left) and sameTree(p.right, q.right)

def subtree(tree, subtree):
    if subtree is None:
        return True
    if tree is None:
        return False
    if sameTree(tree, subtree):
        return True
    return subtree(tree.left, subtree) or subtree(tree.right, subtree)
    