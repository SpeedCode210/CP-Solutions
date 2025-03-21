# Problem: Minimum Size Subarray Sum - https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        nums.append(0)
        p0 = 0
        p1 = 0
        somme = nums[0]
        res = 100000000
        while p1 < len(nums):
            if somme == target:
                res = min(res, p1-p0+1)
                somme -= nums[p0]
                p0 += 1
            elif somme > target:
                somme -= nums[p0]
                p0 += 1
            else:
                p1 += 1
                if p1 < len(nums):
                    somme += nums[p1]
        return res if res != 100000000 else 0