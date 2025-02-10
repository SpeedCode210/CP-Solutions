# Problem: House Robber II - https://leetcode.com/problems/house-robber-ii/

class Solution:
    def super_rob(self, nums: List[int]) -> int:
        dp = [0]*(len(nums)+2)
        for i in range(2,len(nums)+2):
            dp[i] = max(nums[i-2] + dp[i-2], dp[i-1])
        return max(dp[-1],dp[-2])

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.super_rob(nums[:-1]),self.super_rob(nums[1:]))