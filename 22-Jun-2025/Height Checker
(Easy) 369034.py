# Problem: Height Checker
(Easy) - https://leetcode.com/problems/height-checker/

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        a = sorted(heights)
        return sum([0 if a[i] == heights[i] else 1 for i in range(len(heights))])