# Problem: Sum of Two Integers - https://leetcode.com/problems/sum-of-two-integers/description/

class Solution:
    def getSum(self, a: int, b: int) -> int:
        ad = 0
        res = 0

        for i in range(32):
            res ^= (a^b)&(1<<i)
            res ^= ad<<i
            if (ad and (0 != a&(1<<i))) or (ad and (0 != b&(1<<i))) or (0 != (b&(1<<i)) and (0 != a&(1<<i))):
                ad = 1
            else:
                ad = 0
        if (1<<31)&res:
            x = (res^0b11111111111111111111111111111111)
            i = 0
            while x& (1<<i):
                x ^= 1<<i
                i += 1
            x ^= 1<<i
            return -x
        return res