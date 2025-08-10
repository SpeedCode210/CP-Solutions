# Problem: Is Subsequence - https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        p = 0
        for x in t:
            if s[p] == x:
                p += 1
            if p == len(s):
                return True
        return False