# Problem: Roman to Integer - https://leetcode.com/problems/roman-to-integer/?envType=problem-list-v2&envId=string

class Solution:
    def romanToInt(self, s: str) -> int:
        s = s + " "
        res = 0
        for i in range(len(s)-1):
            if s[i] == "I":
                res += 1*(-1 if (s[i+1] == 'V' or s[i+1] == 'X' ) else 1)
            elif s[i] == 'X':
                res += 10*(-1 if (s[i+1] == 'L' or s[i+1] == 'C') else 1)
            elif s[i] == 'C':
                res += 100*(-1 if (s[i+1] == 'D' or s[i+1] == 'M') else 1)
            elif s[i] == 'V':
                res += 5
            elif s[i] == 'L':
                res += 50
            elif s[i] == 'D':
                res += 500
            elif s[i] == 'M':
                res += 1000
        
        return res

        