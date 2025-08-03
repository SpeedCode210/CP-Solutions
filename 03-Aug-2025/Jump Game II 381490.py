# Problem: Jump Game II - https://leetcode.com/problems/jump-game-ii/description/

class Solution:
    def jump(self, nums: List[int]) -> int:
        res = [1000000000]*len(nums)
        res[0] = 0
        for i in range(len(nums)):
            for j in range(1,min(len(nums)-i, nums[i]+1)):
                res[i+j] = min(res[i+j], res[i]+1)
        return res[-1]