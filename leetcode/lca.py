def lacofBT(root, node1, node2):
    if not root:
        return None
    
    if node1 == root.val or node2 == root.val:
        return root
    
    l = lacofBT(root.left, node1, node2)
    r = lacofBT(root.right, node1, node2)

    if l and r:
        return root
    else:
        return l or r  