def productExceptSelf(nums):
    
    res = [1]

    for i in range(1, len(nums)):
        res.append(res[i-1]*nums[i-1])
    
    rp = 1

    for i in range(len(nums)-1, -1, -1):
        res[i] = rp * res[i]
        rp *= nums[i]

    return res

nums = [1,2,3,4]
print(productExceptSelf(nums))
