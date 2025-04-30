# Problem: K Radius Subarray Averages - https://leetcode.com/problems/k-radius-subarray-averages/description/

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        res = [-1]*len(nums)
        som = 0
        for i in range(len(nums)):
            som += nums[i]
            if i - 2*k - 1 >= 0:
                som -= nums[i - 2*k - 1] 
            if i - 2*k >= 0:
                res[i-k] = som//(2*k+1)
        return res