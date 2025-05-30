# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

from collections import defaultdict
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        d = defaultdict(int)
        d[0] = 1
        last = 0
        res = 0
        for c in nums:
            last += c
            res += d[last - goal]
            d[last] += 1
        return res