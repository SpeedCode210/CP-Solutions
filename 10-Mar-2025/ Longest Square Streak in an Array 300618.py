# Problem:  Longest Square Streak in an Array - https://leetcode.com/problems/longest-square-streak-in-an-array/description/?envType=problem-list-v2&envId=sorting

from collections import defaultdict
from math import sqrt
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        D = defaultdict(set)
        for c in nums:
            C = c
            n = 1
            while True:
                if floor(sqrt(C)) == sqrt(C):
                    C = sqrt(C)
                    n += 1
                else:
                    D[C].add(n)
                    break
        res = -1
        for x in D:
            s = sorted([f for f in D[x]])
            u = 1
            for i in range(1, len(s)):
                if s[i] == s[i-1] + 1:
                    u += 1
                else:
                    break
            if u > 1:
                res = max(u, res)
        return res
