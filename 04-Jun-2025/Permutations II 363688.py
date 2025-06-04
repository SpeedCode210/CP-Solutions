# Problem: Permutations II - https://leetcode.com/problems/permutations-ii/description/

class Solution:
    def permuteUnique(self, nums: List[int], cache = None) -> List[List[int]]:
        if cache is None:
            cache = [0]*len(nums)
            nums.sort()
        res = []
        i = 0
        while i < len(cache):
            if cache[i] == 0:
                cache[i] = 1
                for x in self.permuteUnique(nums, cache):
                    res.append([nums[i]] + x)
                cache[i] = 0
                l = nums[i]
                while i < len(cache) and nums[i] == l:
                    i += 1
            else:
                i += 1
        if len(res) == 0:
            return [[]]
        return res