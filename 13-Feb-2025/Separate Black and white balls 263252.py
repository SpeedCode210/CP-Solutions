# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        p = 0
        res = 0
        for i in range(len(s)):
            if s[i] == "0":
                res += i - p
                p += 1
        return res