# Problem: Bitwise AND of Numbers Range - https://leetcode.com/problems/bitwise-and-of-numbers-range/

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        res = 0
        for i in range(32):
            if (1<<i)&right and ((right^(1<<i))|((1<<i)-1)) < left:
                res += (1<<i)
        return res