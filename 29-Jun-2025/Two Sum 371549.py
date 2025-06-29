# Problem: Two Sum - https://leetcode.com/problems/two-sum/description

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        S = dict()
        for i in range(0, len(nums)):
            if target - nums[i] in S:
                return [S[target - nums[i]], i]
            S[nums[i]] = i
