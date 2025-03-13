# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        res = True
        for i in range(len(s)):
            if s[i] != s[-i-1]:
                res = False
        if res :
            return True
        
        p0,p1 = 0,len(s)-1
        skips = 1
        res = True

        while p0 < p1:
            if s[p0] != s[p1]:
                if skips == 0:
                    res = False
                    break
                else:
                    p1 -= 1
                    skips -= 1
            else:
                p1 -= 1
                p0 += 1
        if res :
            return True
        p0,p1 = 0,len(s)-1
        skips = 1
        res = True

        while p0 < p1:
            if s[p0] != s[p1]:
                if skips == 0:
                    res = False
                    break
                else:
                    p0 += 1
                    skips = 0
            else:
                p1 -= 1
                p0 += 1

        return res