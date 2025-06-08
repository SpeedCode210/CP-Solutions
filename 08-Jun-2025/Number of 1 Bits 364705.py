# Problem: Number of 1 Bits - https://leetcode.com/problems/number-of-1-bits/description/

class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 0: 
            return 0
        return n%2 + self.hammingWeight(n//2)