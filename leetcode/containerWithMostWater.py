def containerWater(height):

    l = 0
    r = len(height) - 1
    area = 0

    while l < r:
        left_h = height[l]
        right_h = height[r]

        min_height = min(left_h, right_h)
        area = max(area, min_height*(r-l))

        if left_h < right_h:
            l += 1
        else:
            r -= 1
    return area

height = [1,8,6,2,5,4,8,3,7]

print(containerWater(height))