# Problem: Longest Repeating Character Replacement - https://leetcode.com/problems/longest-repeating-character-replacement/

from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        p0 = 0
        D = defaultdict(int)
        for p1 in range(len(s)):
            D[s[p1]] += 1
            u = max([D[c] for c in D])
            
            while p1 - p0 + 1 - u > k:
                D[s[p0]] -= 1
                u = max([D[c] for c in D])
                p0 += 1

            res = max(res, p1 - p0 + 1)

        return res