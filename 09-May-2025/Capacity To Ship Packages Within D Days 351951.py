# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        a = max(weights)
        b = sum(weights)

        while a < b:
            m = (a+b)//2
            x = 0
            tot = m
            for w in weights:
                if tot+w <= m:
                    tot += w
                else:
                    x += 1
                    tot = w
            if x <= days:
                b = m
            else:
                a = m+1

        return a