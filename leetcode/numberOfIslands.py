def create_adjaceny_list_undirected(edges):
    adj_list = {}

    for u, v in edges:
        if u not in adj_list:
            adj_list[u] = []
        if v not in adj_list:
            adj_list[v] = []
        adj_list[u].append(v)
        adj_list[v].append(u)
    return adj_list


def create_adj_list_directed(edges):
    adj_list = {}

    for u, v in edges:
        if u not in adj_list:
            adj_list[u] = []
        adj_list[u].append(v)

    return adj_list


edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'F'), ('E', 'F')]
adj = create_adj_list_directed(edges)


def calculate_indegree(edges):
    # Initialize indegree for all nodes
    indegree = {}
    for u, v in edges:
        if u not in indegree:
            indegree[u] = 0  # u is a source
        if v not in indegree:
            indegree[v] = 0  # Initialize v
        indegree[v] += 1  # Increment indegree for target node
    return indegree


indegree = calculate_indegree(edges)
print(adj)
print(indegree)