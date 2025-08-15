# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0]*target
        for i in range(1, target+1):
            for x in nums:
                dp[i] += dp[i-x] if i-x >= 0 else 0
        return dp[-1]