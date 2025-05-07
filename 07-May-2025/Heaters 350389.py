# Problem: Heaters - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        res = 0
        for h in houses:
            if h < heaters[0]:
                res = max(res, heaters[0] - h)
            elif h > heaters[-1]:
                res = max(res, h - heaters[-1])
            else:
                a = 0
                b = len(heaters)-1
                while a < b:
                    m = (a+b)//2
                    if heaters[m] < h:
                        a = m+1
                    else:
                        b = m
                res = max(res, min(heaters[a]-h, h-heaters[a-1]))
        return res
