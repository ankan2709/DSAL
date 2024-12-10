import math

def minOps(n):
    if (n == pow(2, int(math.log2(n)))):
        return 1
    
    low = pow(2, int(math.log2(n)))
    high = pow(2, int(math.log2(n) + 1))

    d1 = n - low
    d2 = high - n

    return 1 + min(minOps(d1), minOps(d2))

print(minOps(54))