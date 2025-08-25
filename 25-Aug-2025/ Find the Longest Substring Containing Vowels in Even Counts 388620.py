# Problem:  Find the Longest Substring Containing Vowels in Even Counts - https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/description/

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        last = {0 : -1}
        res = 0
        curr = 0
        for i in range(len(s)):
            if s[i] in 'aeoiu':
                curr ^= 1<<(ord(s[i])-ord('a'))
            
            if curr in last:
                res = max(res, i - last[curr])
            else:
                last[curr] = i
        return res