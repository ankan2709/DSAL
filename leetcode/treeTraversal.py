def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


def preorder(root):
    if root is not None:
        print(root.val)
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.val)
