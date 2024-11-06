def squareRoot(num):
    if num == 0:
        return 0
    left = 1
    right = num
    res = 0
    while left <= right:
        mid = (left + right) // 2

        square = mid*mid

        if square <= num:
            res = mid
            l = mid + 1
        else:
            r = mid - 1
    return res

print(squareRoot(9))
