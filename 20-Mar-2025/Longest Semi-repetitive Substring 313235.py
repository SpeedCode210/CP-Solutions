# Problem: Longest Semi-repetitive Substring - https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        pairs = 0
        p1 = 0
        res = 1
        for p2 in range(1, len(s)):
            if s[p2-1] == s[p2]:
                pairs += 1
            while pairs == 2:
                if s[p1] == s[p1+1]:
                    pairs -= 1
                p1 += 1
            res = max(res, p2 - p1 + 1)
        return res