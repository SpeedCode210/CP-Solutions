# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        arr = [0]*(len(nums)+1)
        arr[-2] = 1
        for i in range(len(nums)-2, -1, -1):
            if arr[i+1] - arr[min(len(nums), i + nums[i]+1)] > 0:
                arr[i]  = arr[i+1]+ 1
            else:
                arr[i] = arr[i+1]
        return arr[0] > arr[1]