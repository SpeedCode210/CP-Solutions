# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0:
            return True
        if floor(sqrt(c))*floor(sqrt(c)) == c:
            return True
        i = 2
        while i*i <= c:
            u = 0
            while c%i == 0:
                c = c // i
                u += 1
            if i%4 == 3 and u%2 == 1:
                return False
            i += 1
        
        return c%4 != 3