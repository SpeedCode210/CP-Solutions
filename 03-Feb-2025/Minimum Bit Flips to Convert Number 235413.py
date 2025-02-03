# Problem: Minimum Bit Flips to Convert Number - https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        h = start ^ goal
        counter = 0
        while h > 0:
            if h%2 == 1:
                counter += 1
            h = h // 2
        return counter