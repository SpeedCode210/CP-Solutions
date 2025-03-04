# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

from collections import Counter
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        C = Counter([x for x in s])
        return "1"*(C["1"]-1) + "0"*C["0"] + "1"