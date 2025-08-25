# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        if x == y:
            return 0
        return abs(x-y)%2 + self.hammingDistance(x//2, y//2)