# Problem: Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/submissions/

from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = (0, len(s) + 2)
        p0 = 0
        d = defaultdict(int)
        c = Counter([c for c in t])
        i = len(set([c for c in t]))
        u = 0
        flag = False
        for p1 in range(len(s)):
            if d[s[p1]] >= c[s[p1]]:
                u -= 1
            d[s[p1]] += 1
            if d[s[p1]] >= c[s[p1]]:
                u += 1

            if u == i and res[1] - res[0] >= p1 - p0 + 1:
                res = (p0,p1+1)
                flag = True

            while u == i:
                if res[1] - res[0] >= p1 - p0 + 1:
                    res = (p0,p1+1)
                d[s[p0]] -= 1
                if d[s[p0]] < c[s[p0]]:
                    u -= 1
                p0 += 1

        return s[res[0]:res[1]] if len(s) >= res[1] - res[0] else ""