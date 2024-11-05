def create_graph(vertices, edges):
    adj_list = {}

    for i in range(vertices):
        adj_list[i] = []

    for item in edges:
        u = item[0]
        v = item[1]
        adj_list[u].append(v)
    return adj_list 
n = 5
edges = [[1, 2], [1, 0], [2, 0], [2, 3], [2, 4]]

# graph = create_graph(n, edges)
# print(graph)

graph = {
    0: [],
    1: [2, 0],
    2: [4, 3, 0],  # Reversing the order here
    3: [],
    4: []
}

# DFS
visited = [False]*n
result = []

def DFS(graph, u, visited, result):
    if visited[u] == True:
        return
    visited[u] = True
    result.append(u)
    for v in graph[u]:
        if visited[v] == False:
            DFS(graph, v, visited,result)

# DFS(graph, 1, visited, result)
# print(result)


# BFS
visited = [False]*n
result = []

def BFS(graph, start_vertex, visited, result):

    """
    time complexity : o(v) + o(e)
    space : o(v)
    """
    queue = []
    visited[start_vertex] = True
    result.append(start_vertex)
    queue.append(start_vertex)

    while queue:
        u = queue.pop(0)
        for v in graph[u]:
            if visited[v] == False:
                queue.append(v)
                visited[v] = True
                result.append(v)


# BFS(graph, 1, visited, result)
# print(result)


#############

graph = {
    0: [1],
    1: [0, 2],
    2: [1, 3, 4],
    3: [2, 4],
    4: [2, 3]
}

def detectCycle_undirected_DFS(graph, u, visited, parent):
    visited[u] = True
    for v in graph[u]:
        if v == parent:
            continue
        if visited[v] == True:
            return True      
        if detectCycle_undirected_DFS(graph, v, visited, u) == True:
            return True
    return False


visited = [False]*n
has_cycle = False
for i in range(n):
    if not visited[i]:  # Check every unvisited component
        if detectCycle_undirected_DFS(graph, i, visited, -1):  # Initial parent is set to -1 (no parent)
            has_cycle = True
            break
print(has_cycle)