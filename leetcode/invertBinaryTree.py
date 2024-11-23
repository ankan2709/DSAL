def invertBT(root):
    if not root:
        return
    root.left, root.right = root.right, root.left

    invertBT(root.left)
    invertBT(root.right)
    return root

