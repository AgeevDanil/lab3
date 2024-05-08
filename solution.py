import random
class Solution:
    def __init__(self):
        pass

    def quicksort(self, nums):
        if len(nums) <= 1:
            return nums
        else:
            q = random.choice(nums)
        l_nums = [n for n in nums if n < q]
        
        e_nums = [q] * nums.count(q)
        b_nums = [n for n in nums if n > q]
        return self.quicksort(l_nums) + e_nums + self.quicksort(b_nums)