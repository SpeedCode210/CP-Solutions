# Problem: The Maximum Number - https://leetcode.com/problems/third-maximum-number/description/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = [x for x in set(nums)]
        nums.sort()
        return nums[-3] if len(nums) > 2 else nums[-1]