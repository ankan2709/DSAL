def bs(arr):

    l = 0
    r = len(arr) - 1

    while l <= r:
        mid = l + ((r - l) // 2)

        if ((mid - 1 < 0 or arr[mid] != arr[mid-1]) and 
             (mid + 1 == len(arr) or arr[mid] != arr[mid+1])):
            return arr[mid]
        
        leftSize = mid - 1 if arr[mid - 1] == arr[mid] else mid

        if leftSize % 2:
            r = mid - 1
        else:
            l = mid + 1
        

arr = nums = [1, 1, 2, 2, 3, 4, 4, 5, 5]
print(bs(arr))