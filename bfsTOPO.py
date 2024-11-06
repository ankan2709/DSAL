# step 1: find indegree
# step 2: put nodes with indegree == 0 in the queue
# step 3: do BFS

indegree = [0] * len(adj)

for u in range(len(adj)):
    for v in adj[u]:
        indegree[v] += 1

q = deque()
for i in range(len(indegree)):
    if indegree[i] == 0:
        q.append(i)

res = []
while q:
    u = q.popleft()
    res.append(u)
    for v in adj[u]:
        indegree[v] -= 1
        if indegree[v] == 0:
            q.append(v)

return res




