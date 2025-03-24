# Problem: Smallest Even Multiple - https://leetcode.com/problems/smallest-even-multiple/

class Solution(object):
    def smallestEvenMultiple(self, n):
        return 2*n if n%2 == 1 else n