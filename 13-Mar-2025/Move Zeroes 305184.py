# Problem: Move Zeroes - https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        p0 = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[p0],nums[i] = nums[i],nums[p0]
                p0 += 1
        