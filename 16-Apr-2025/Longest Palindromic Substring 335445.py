# Problem: Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = (0,0)
        for i in range(len(s)): # odd ones
            for j in range(1, min(i,len(s)-i-1) + 1):
                if s[i-j] == s[i+j]:
                    if 2*j + 1 > res[1] - res[0] + 1:
                        res = (i-j, i+j)
                else :
                    break

        for i in range(len(s)-1): # even ones
            for j in range(0, min(i+1,len(s)-i-1)):
                if s[i-j] == s[i+j+1]:
                    if 2*(j+1) > res[1] - res[0] + 1:
                        res = (i-j, i+j+1)
                else :
                    break
        return s[res[0]:res[1]+1]