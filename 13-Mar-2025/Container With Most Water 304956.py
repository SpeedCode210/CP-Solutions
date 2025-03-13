# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        p0,p1 = 0, len(height)-1
        res = (p1-p0)*min(height[p1],height[p0])
        while p0 < p1:
            if height[p0] > height[p1]:
                p1 -= 1
            else:
                p0 += 1
            res = max(res, (p1-p0)*min(height[p1],height[p0]))
        return res