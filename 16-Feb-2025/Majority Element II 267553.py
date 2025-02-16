# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        C = Counter(nums)
        return [x for x in C if C[x] > (len(nums)//3)]