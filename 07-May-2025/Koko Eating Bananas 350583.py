# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        a = 1
        b = 1000000000
        piles.sort()
        while a < b:
            m = (a+b)//2
            X = sum([(c+m-1)//m for c in piles])
            if X <= h:
                b = m
            else:
                a = m+1
        return a