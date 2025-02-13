# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

from collections import Counter

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res = []
        c = Counter(nums)
        for x in c:
            if(c[x] > 1):
                res.append(x)
            if(c[x] > 2):
                res.append(x)
        return res