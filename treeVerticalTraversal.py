def verticalOrder():

    if not root:
        return []
    
    column_items = collections.defaultdict(list)

    queue = collections.deque([(0, root)])

    res = []

    min_x = float('inf')
    max_x = float('-inf')

    while queue:
        x, node = queue.pop()

        column_items[x].append(node.val)
        min_val = min(x, min_x)
        max_val = max(x, max_x)

        if node.left:
            queue.append((x-1, node.left))
        if node.right:
            queue.append((x+1, node.right))

    for i in range(min_x, max_x+1):
        res.append(column_items[i])