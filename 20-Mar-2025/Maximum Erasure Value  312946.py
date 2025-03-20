# Problem: Maximum Erasure Value  - https://leetcode.com/problems/maximum-erasure-value/

from collections import defaultdict
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        d = defaultdict(int)
        l = 0
        maxi = nums[0]
        d[nums[0]] += 1
        somme = nums[0]
        for r in range(1, len(nums)):
            d[nums[r]] += 1
            somme += nums[r]
            while d[nums[r]] == 2 :
                d[nums[l]] -= 1
                somme -= nums[l]
                l += 1
            maxi = max(somme, maxi)
        return maxi