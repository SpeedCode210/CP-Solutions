# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        a = 1
        while a <= num:
            a <<= 1
        a -= 1
        return ~num & a