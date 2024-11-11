from collections import defaultdict
from heapq import heappop, heappush

def taskScheduler(tasks, n):

    counts = defaultdict(int)

    for item in tasks:
        counts[item] += 1

    heap = [] # need min heap

    for key, val in counts.items():
        heappush(heap, (-val, key))

    time = 0
    while heap:
        temp = []
        for i in range(n+1):
            freq, key = heappop(heap)
            freq -= 1

            temp.append((freq, key))

        for item in temp:
            if item[0] != 0:
                heappush(item)

        if not heap:
            time += 1
        else:
            time += n+1

    return time