# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [[nums[0],0]]
        if len(nums) > 1:
            dp.append([nums[1], nums[0]])
        for i in range(2, len(nums)):
            dp.append([nums[i] + max(dp[-2]), max(dp[-1])])
        return max(dp[-1])