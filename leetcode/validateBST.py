def validateBST(left_val, root, right_val):
    if not root:
        return True
    
    if not (left_val < root.val < right_val):
        return False
    
    return validateBST(float('-inf'), root.left, root) and validateBST(root, root.right, float('inf'))

print(validateBST(float('-inf'), root, float('inf')))