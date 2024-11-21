def construct(preorder, inorder, start, end, idx):

    if start > end:
        return None

    root_val = preorder[idx[0]]
    root_index = inorder.index(root_val)

    idx[0] += 1

    root_node = ListNode(root_val)
    root_node.left = construct(preorder, inorder, start, root_index-1, idx)
    root_node.right = construct(preorder, inorder, root_index + 1, end, idx)

    return root_node

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

n = len(preorder)
idx = [0]
construct(preorder, inorder, 0, n-1 , idx)