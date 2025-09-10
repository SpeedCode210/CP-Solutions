# Problem: First Missing Positive - https://leetcode.com/problems/first-missing-positive/description/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] = max(nums[i], 0)

        for i in range(len(nums)):
            while nums[i] > 0:
                if nums[i] == i+1:
                    nums[i] = -1
                elif nums[i] <= len(nums):
                    if nums[nums[i]-1] > 0:
                        nums[nums[i]-1], nums[i] = -1, nums[nums[i]-1]
                    else:
                        u = nums[i]-1
                        nums[i] = 0
                        nums[u] = -1
                else:
                    nums[i] = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                return i+1
                
        return len(nums)+1
