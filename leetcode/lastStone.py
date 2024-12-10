from heapq import heappop, heappush, heapify

stones = [2,7,4,1,8,1]

maxheap = []
for i in range(len(stones)):
    heappush(maxheap, -stones[i])

while len(maxheap) > 1:
    h1 = - heappop(maxheap)
    h2 = - heappop(maxheap)

    if h1 != h2:
        heappush(maxheap, -(h1-h2))

print(-maxheap[0])