def serialize(root):
    res = []

    def dfs(root):
        if not root:
            res.append('x')
            return
        res.append(str(root.val))
        dfs(root.left)
        dfs(root.right)

    return "".join(res)

def deserialize(s):
    values = s.split()
    i = 0

    def buildTreeDfs():
        if  values[i] == 'x':
            i += 1
            return
        node = Node(values[i])
        i += 1
        node.left = dfs()
        node.right = dfs()
        return node
    buildTreeDfs()