# def combine(n, k):


#     def solve(start, n, k, temp):
#         if k == 0:
#             res.append(temp[:])
#             return
#         if start > n:
#             return 
        
#         temp.append(start)
#         solve(start+1, n, k-1, temp)

#         temp.pop()
#         solve(start+1, n, k, temp)

#     res = []
#     solve(1, n, k, [])
#     return res

# print(combine(4, 2))

def combine(n, k):
    def solve(start, n, k, temp):
        if k == 0:
            res.append(temp[:])
            return
        
        for i in range(start, n + 1):
            temp.append(i)
            solve(i + 1, n, k - 1, temp)
            temp.pop()  # Backtrack

    res = []
    solve(1, n, k, [])
    return res

print(combine(4, 2))
