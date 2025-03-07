# Problem: Largest Number (Optional) - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(n) for n in nums]
        for _ in range(len(nums)):
            for i in range(len(nums) - 1):
                if nums[i] + nums[i+1] < nums[i+1] + nums[i]:
                    nums[i], nums[i+1] = nums[i+1],nums[i]
        s = "".join(nums)
        while len(s) > 1 and s[0:2] == "00":
            s = s[1:]
        return s