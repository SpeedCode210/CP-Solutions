# Problem: Majority Element - https://leetcode.com/problems/majority-element/description/

from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        target = len(nums) // 2 + 1
        hi = defaultdict(int)
        for x in nums:
            hi[x] += 1
            if hi[x] >= target:
                return x
        