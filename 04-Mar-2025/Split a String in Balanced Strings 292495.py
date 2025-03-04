# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        hi = 0
        count = 0
        for c in s:
            hi += 1 if c == "L" else -1
            if hi == 0:
                count += 1
        return count

        