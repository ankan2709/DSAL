class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topologicalSort(self,adj):
        # Code here
        def DFS(adj, u, visited, stack):
            visited[u] = True
            
            for v in adj[u]:
                if not visited[v]:
                    DFS(adj, v, visited, stack)
                    
            stack.append(u)
            
        visited = [False] * len(adj)
        stack = []
        
        for i in range(len(adj)):
            if not visited[i]:
                DFS(adj, i, visited, stack)

            
        return stack[::-1]
            
            
            
#{ 
 # Driver Code Starts
# Driver Program

import sys

sys.setrecursionlimit(10**6)


def check(graph, N, res):
    if N != len(res):
        return False
    map = [0] * N
    for i in range(N):
        map[res[i]] = i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True


if __name__ == '__main__':
    t = 10
    for i in range(t):
        e, N = list(map(int, input().strip().split()))
        adj = [[] for i in range(N)]

        for i in range(e):
            u, v = map(int, input().split())
            adj[u].append(v)

        ob = Solution()

        res = ob.topologicalSort(adj)

        if check(adj, N, res):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends