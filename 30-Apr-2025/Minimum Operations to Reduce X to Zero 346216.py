# Problem: Minimum Operations to Reduce X to Zero - https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        t = sum(nums) - x
        if t < 0:
            return -1
        res = 1000000000
        som = 0
        p0 = 0

        for i in range(n):
            som += nums[i]
            while som > t:
                som -= nums[p0]
                p0 += 1

            if som == t:
                res = min(res, p0 + n - i - 1)

        return -1 if res == 1000000000 else res
