from collections import defaultdict, deque

def courseScheduler(n, prereq):

    graph = defaultdict(list)
    for item in prerequisites:
        u = item[1]
        v = item[0]
        graph[u].append(v)

    indegree = [0]*n
    for u in range(n):
        for v in graph[u]:
            indegree[v] += 1

    queue = deque()
    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)

    res = []
    while queue:
        u = queue.popleft()
        res.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

    return True if n == len(res) else False

n = 2
prerequisites = [[0, 1]]
print(courseScheduler(n, prerequisites))