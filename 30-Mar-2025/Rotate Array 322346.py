# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        u = nums[n-k:] + nums[:n-k]
        for i in range(len(u)):
            nums[i] = u[i]
        