import heapq

def kthSmallest(matrix, k):
    heap = []

    seen = set()

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            val = matrix[i][j]

            if val in seen:
                continue
            seen.add(val)
            
            if len(heap) < k:
                heapq.heappush(heap, -val)
            else:
                heapq.heappop()
    print(heap[0])
    return None

matrix = [[1,5,9],[10,11,13],[12,13,15]]

# matrix = [[1,1,3],[1,2,3],[1,4,5]]
k = 8

print(kthSmallest(matrix, k))