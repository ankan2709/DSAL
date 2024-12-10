# def isUgly(num):
#     factors = [2,3,5]

#     for factor in factors:
#         while num % factor == 0:
#             num //= factor
#     return num == 1

# def nthUgly(n):
#     res = []
#     i = 1
#     while len(res) != n:
#         if isUgly(i):
#             res.append(i)
#         i += 1

#     return res[-1]

# print(nthUgly(10))
