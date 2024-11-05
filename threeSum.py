def threeSum(nums):

    three_sum_res = []

    for i in range(len(nums)):
        target = -(nums[i])

        left = i + 1
        right = len(nums) - 1

        while left < right:
            total = nums[left] + nums[right]
            if total == target:
                three_sum_res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif total < target:
                left += 1
            else:
                right -= 1

    return three_sum_res

nums = [-1,0,1,2,-1,-4]
nums.sort()
# target =  0
result = threeSum(nums)
print(result)



        


    

