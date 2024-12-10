import collections

def levelOrder(root):
    if not root:
        return []
    
    queue = collections.deque()
    res = []
    queue.append(root)

    while queue:
        n = len(queue)
        level = []

        for i in range(n):
            curr = queue.popleft()

            if curr:
                level.append(curr.val)
                queue.append(curr.left)
                queue.append(curr.right)
        if level:
            res.append(level)

