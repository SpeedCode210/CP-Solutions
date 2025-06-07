# Problem: Count Complete Subarrays in an Array - https://leetcode.com/problems/count-complete-subarrays-in-an-array/

from collections import defaultdict
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        d = defaultdict(int)
        s = len(set(nums))
        right = 0
        s -= 1
        d[nums[0]] = 1
        res = 0
        for i in range(len(nums)):
            while s > 0:
                right += 1
                if right == len(nums):
                    return res
                d[nums[right]] += 1
                if d[nums[right]] == 1:
                    s -= 1
            res += len(nums) - right
            d[nums[i]] -= 1
            if d[nums[i]] == 0:
                s += 1
                
        return res