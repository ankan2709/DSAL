import random

class Solution:

    def __init__(self, nums):
        self.original = nums[:]
        self.array = nums[:]

    def reset(self):
        self.array = self.original[:]
        return self.array

    def shuffle(self):
        shuffled = self.array[:]
        n = len(shuffled)
        for i in range(n):
            swap_idx = random.randint(i, n-1)
            shuffled[i], shuffled[swap_idx] = shuffled[swap_idx], shuffled[i]

        return shuffled
        


# Your Solution object will be instantiated and called as such:
solution = Solution([1, 2, 3])
print(solution.shuffle())  # Random output, e.g., [3, 1, 2]
print(solution.reset())    # Output: [1, 2, 3]
print(solution.shuffle()) 