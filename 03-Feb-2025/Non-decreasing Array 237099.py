# Problem: Non-decreasing Array - https://leetcode.com/problems/non-decreasing-array/

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        k = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                k += 1
        if k == 1 and (nums[0] > nums[1] or nums[-1] < nums[-2]):
            return True
        if k == 0 :
            return True
        if k > 2:
            return False
        for i in range(1,len(nums)-1):
            y = 0
            if nums[i] < nums[i-1]:
                y += 1
            if nums[i+1] < nums[i]:
                y += 1
            if k == y and nums[i+1] >= nums[i-1]:
                return True
        return False