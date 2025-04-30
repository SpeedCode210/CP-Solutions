# Problem: Power of Four - https://leetcode.com/problems/power-of-four/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0:
            return False
        return self.isPowerOfFour(n//4) if n%4 == 0 else n == 1