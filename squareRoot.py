def squareRoot(num):
    i = 0
    left = 0
    right = num
    res = -1
    while left <= right:
        mid = (left + right) // 2

        if mid*mid == num:
            return mid
        elif mid*mid < num:
            res = mid
            left = mid 
        else:
            right = mid - 1
    return res

print(squareRoot(9))
