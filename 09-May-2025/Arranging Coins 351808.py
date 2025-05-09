# Problem: Arranging Coins - https://leetcode.com/problems/arranging-coins/description/

class Solution:
    def arrangeCoins(self, n: int) -> int:
        a = 1
        b = 2**30 + 2

        while a < b:
            m = (a+b+1)//2
            if m*(m+1)//2 <= n:
                a = m
            else:
                b = m-1

        return a
        