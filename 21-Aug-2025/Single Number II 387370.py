# Problem: Single Number II - https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = [0]*23
        for x in nums:
            i = 0
            if x < 0:
                res[22] += 1
                res[22] %= 3
                x = -x
            while x:
                res[i] = (x+res[i])%3
                x //= 3
                i += 1
        return sum([res[i]*(3**i) for i in range(22)])*((-1)**res[22])
