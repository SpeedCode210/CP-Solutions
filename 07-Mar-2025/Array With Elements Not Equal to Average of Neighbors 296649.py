# Problem: Array With Elements Not Equal to Average of Neighbors - https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        return [nums[(-1)**i * (i//2 + i%2)] for i in range(len(nums))]