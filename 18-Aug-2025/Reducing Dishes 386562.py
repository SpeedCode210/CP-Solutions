# Problem: Reducing Dishes - https://leetcode.com/problems/reducing-dishes/

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        h = [0]
        b = [0]
        res = 0
        for i in range(len(satisfaction)):
            h.append(h[-1] + satisfaction[i])
            b.append(b[-1] + satisfaction[i]*(len(satisfaction)-i))
            res = max(res, b[-1] - h[-1]*(len(satisfaction)-i-1))
        return res