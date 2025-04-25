# Problem: Continuous Subarray Sum - https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        a = set([0])
        beforeLast = nums[0]%k
        for i in range(1, len(nums)):
            if (beforeLast + nums[i])%k in a:
                return True
            a.add(beforeLast)
            beforeLast = (beforeLast + nums[i])%k
        return False