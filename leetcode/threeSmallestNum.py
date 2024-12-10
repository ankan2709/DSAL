from heapq import heapify, heappop, heappush

def heap_top_3(arr):
    heapify(arr)

    res = []
    for i in range(3):
        res.append(heappop(arr))
    return res

