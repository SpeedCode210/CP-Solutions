# Problem: Build Array from Permutation - https://leetcode.com/problems/build-array-from-permutation/description/

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        K = 1 << 11
        for i in range(len(nums)):
            nums[i] = nums[i] + ((nums[nums[i]%K]%K) << 11)
        
        for i in range(len(nums)):
            nums[i] = nums[i] >> 11
            
        return nums
