class SparseVec:
    def __init__(self, nums):
        self.hashmap = {}

        for i, val in enumerate(nums):
            if val:
                self.hashmap[i] = val

    def dotProduct(self, vec):
        res = 0
        for key, val in vec.hashmap.items():
            if key in self.hashmap:
                res += val * self.hashmap[key]

        return res