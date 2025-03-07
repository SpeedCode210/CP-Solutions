# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            pass
        elif len(nums) == 2:
            if nums[0] > nums[1]:
                nums[0], nums[1] = nums[1],nums[0]
        else:
            for i in range(len(nums)):
                nums[nums[i]%4] += 4
                print(nums)
            for i in range(nums[0]//4):
                nums[i] = (nums[i]//4)*4
            for i in range(nums[0]//4, nums[0]//4 + nums[1]//4):
                nums[i] = (nums[i]//4)*4 + 1
            for i in range(nums[0]//4 + nums[1]//4, len(nums)):
                nums[i] = (nums[i]//4)*4 + 2
            for i in range(3):
                nums[i] %= 4



        