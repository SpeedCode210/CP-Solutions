# Problem: Append Characters to String to Make Subsequence - https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/description/

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        p0 = 0
        for c in s:
            if c == t[p0]:
                p0 += 1
            if p0 == len(t):
                break
        return (len(t)-p0)