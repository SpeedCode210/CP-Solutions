# Problem: Minimum Deletions to Make String Balanced - https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

class Solution:
    def minimumDeletions(self, s: str) -> int:
        res = 100000000
        a = sum([1 for c in s if c == 'a'])
        b = 0
        res = a
        for c in s:
            if c == 'a':
                a -= 1
                res = min(res, a+b)
            else:
                b += 1
            
        return res