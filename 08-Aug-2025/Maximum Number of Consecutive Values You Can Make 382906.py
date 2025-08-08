# Problem: Maximum Number of Consecutive Values You Can Make - https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/description/

class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        X = 0
        coins.sort()
        for d in coins :
            if d <= X+1:
                X += d
            else:
                return X+1
        return X+1