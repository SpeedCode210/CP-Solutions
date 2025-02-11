# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

from collections import Counter

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        x = Counter(nums)
        return [sum([x[u]//2 for u in x]),sum([x[u]%2 for u in x])]