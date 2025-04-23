# Problem: Clear Digits - https://leetcode.com/problems/clear-digits/description/

class Solution:
    def clearDigits(self, s: str) -> str:
        for i in range(len(s)):
            for j in range(1,len(s)):
                if s[j] >= "0" and s[j] <= "9":
                    s = s[:j-1] + s[j+1:]
                    break
        return s