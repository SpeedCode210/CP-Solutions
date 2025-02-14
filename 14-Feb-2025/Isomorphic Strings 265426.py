# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        a = dict()
        b = dict()
        for i in range(len(s)):
            if s[i] in a and a[s[i]] != t[i]:
                return False
            if t[i] in b and b[t[i]] != s[i]:
                return False
            a[s[i]] = t[i]
            b[t[i]] = s[i]
        return True
        