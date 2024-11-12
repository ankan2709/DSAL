import math
def minOps(n, memo = {}):

    if n == pow(2, int(math.log2(n))):
        return 1
    
    if n in memo:
        return memo[n]
    
    minVal = pow(2, int(math.log2(n)))
    maxVal = pow(2, int(math.log2(n) + 1))

    d1 = n- minVal
    d2 = maxVal - n

    memo[n] = 1 + min(minOps(d1), minOps(d2))
    return memo[n]

print(minOps(51))