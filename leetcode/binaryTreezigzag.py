from collections import deque

def zigzag(root):

    if not root:
        return []
    
    queue = deque
    res = []

    queue.append(root)
    i = 1
    while queue:
        q_len = len(queue)
        level = []

        for i in range(q_len):
            curr_node = queue.popleft()
            if curr_node:
                level.append(curr_node.val)
                queue.append(curr_node.left)
                queue.append(curr_node.right)

        if level:
            if i % 2 == 0:
                res.append(level[::-1])
            else:
                res.append(level)
        i += 1

    return res
                    
