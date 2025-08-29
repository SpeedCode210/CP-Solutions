# Problem: Minimum One Bit Operations to Make Integers Zero - https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/description/?envType=problem-list-v2&envId=bit-manipulation

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n < 2:
            return n
        
        for i in range(32, -1, -1):
            if (n&(1<<i)):
                n ^= (1<<i)
                return (1<<(i+1)) - 1 - self.minimumOneBitOperations(n)
