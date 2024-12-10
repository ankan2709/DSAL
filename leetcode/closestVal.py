def closestValue(root, target):

    inorder_arr = []

    def inorder(root):
        if root is None:
            return

        inorder(root.left)
        inorder_arr.append(root.val)
        inorder(root.right)

    inorder(root)

    res = 0
    min_val = float('inf')
    for i in range(len(inorder_arr)):
        diff = abs(target - inorder_arr[i])
        if diff < min_val:
            res = inorder_arr[i]
            min_val = diff

    return res