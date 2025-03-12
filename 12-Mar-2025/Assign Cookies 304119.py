# Problem: Assign Cookies - https://leetcode.com/problems/assign-cookies

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res = 0
        p = 0
        for c in g:
            while p < len(s):
                if s[p] >= c:
                    res += 1
                    p += 1
                    break
                p += 1
        return res