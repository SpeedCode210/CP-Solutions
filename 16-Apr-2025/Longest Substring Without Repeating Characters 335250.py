# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p0 = 0
        D = defaultdict(int)
        res = 0
        for p1 in range(len(s)):
            D[s[p1]] += 1
            while D[s[p1]] == 2:
                D[s[p0]] -= 1
                p0 += 1
            res = max(res, p1 - p0 + 1)
        return res