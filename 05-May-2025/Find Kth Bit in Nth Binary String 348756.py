# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"
        A = {"1":"0", "0":"1"}
        middle = 2**(n-1)
        if k == middle:
            return "1"
        if k < middle:
            return self.findKthBit(n-1, k)
        return A[self.findKthBit(n-1, 2**n - k)]
