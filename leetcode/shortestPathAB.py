def getNeighbors(node):
    return graph[node]

from collections import deque

def shortestPathBFS(root, target):
    queue = deque()
    queue.append(root)
    level = 0
    visited = set()
    visited.add(root)

    while queue:
        q_len = len(queue)

        for i in range(q_len):
            node = queue.popleft()

            if node == target:
                return level
            for neighbor in getNeighbors(node):
                if neighbor in visited:
                    continue
                queue.append(neighbor)
                visited.add(neighbor)
        level += 1
    return level