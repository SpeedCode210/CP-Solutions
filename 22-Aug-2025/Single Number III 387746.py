# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for x in nums:
            xor ^= x
        i = 1
        while 0 == (xor&i):
            i <<= 1
        res = [0, 0]

        for x in nums:
            res[0 if x&i else 1] ^= x

        return res