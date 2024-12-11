def maxProductSubarray(arr):
    n = len(arr)
    leftProd = 1
    rightProd = 1
    ans = arr[0]

    for i in range(len(arr)):
        if leftProd == 0:
            leftProd = 1
        if rightProd == 0:
            rightProd = 1

        leftProd *= arr[i]
        rightProd *= arr[n-1-i]

        ans = max(ans, leftProd, rightProd)
    return ans


nums = [2,3,-2,4]
print(maxProductSubarray(nums))
nums = [-2,0,-1]
print(maxProductSubarray(nums))