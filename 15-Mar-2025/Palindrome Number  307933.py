# Problem: Palindrome Number  - https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        for i in range(0, len(s)):
            if s[i] != s[len(s)-i-1]:
                return False
        return True
        