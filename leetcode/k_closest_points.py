points = [(1, 1), (2, 2), (3, 3)]
origin = (0, 0)
k = 1

import math
import heapq

def k_closest(points, k):

    heap = []
    for (x,y) in points:
        dist = math.sqrt(x**2 + y**2)
        heapq.heappush(heap, (dist, (x,y)))

    res = []
    for i in range(k):
        res.append(heapq.heappop(heap)[1])

    return res

print(k_closest(points, k))