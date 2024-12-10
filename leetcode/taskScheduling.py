from collections import defaultdict, deque

def taskScheduling(tasks, requirements):

    graph = defaultdict(list)
    for u,v in requirements:
        graph[u].append(v)

    indegree = {task:0 for task in tasks}
    for u, neighbors in graph.items():
        for v in neighbors:
            indegree[v] += 1

    q = deque()
    for node, indeg in indegree.items():
        if indeg == 0:
            q.append(node)

    res = []

    while q:
        u = q.popleft()
        res.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)

    return res if len(graph) == len(res) else None


tasks = ["a", "b", "c", "d"]
requirements = [["a", "b"], ["c", "b"], ["b", "d"]]

print(taskScheduling(tasks, requirements))