# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        C = Counter(nums)
        return [x for x in C if C[x] == 2]