# Problem: First Bad Version - https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        a = 1
        b = n
        while a != b:
            m = (a+b)//2
            if isBadVersion(m):
                b = m
            else:
                a = m+1
        return a