# Problem: Reverse String - https://leetcode.com/problems/reverse-string/description/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = len(s)
        for i in range(0,(n+1)//2):
            c = s[i]
            s[i] = s[n-i-1]
            s[n-i-1] = c
