class SparseDotProductOfVector:
    def __init__(self, nums):
        self.key_val_map = {}

        for i, val in enumerate(nums):
            if val != 0:
                self.key_val_map[i] = val


    def dotProduct(self, vec):
        res = 0

        for key, val in vec.key_val_map.items():
            if key in self.key_val_map:
                res += self.key_val_map[key] * val

        return res
    
nums1 = [1,0,0,2,3]
nums2 = [0,3,0,4,0]
v1 = SparseDotProductOfVector(nums1)
v2 = SparseDotProductOfVector(nums2)
ans = v1.dotProduct(v2)
print(ans)