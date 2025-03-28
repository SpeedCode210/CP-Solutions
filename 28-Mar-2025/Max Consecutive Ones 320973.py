# Problem: Max Consecutive Ones - https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count  = 0
        res = 0
        for c in nums:
            if c == 1:
                count += 1
                res = max(res, count)
            else:
                count = 0
        return res