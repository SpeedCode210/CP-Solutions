# Problem: Target Sum - https://leetcode.com/problems/target-sum/

from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        a = [defaultdict(int) for i in range(n+1)]
        a[0][0] = 1
        for i in range(1,1+n):
            for x in a[i-1]:
                a[i][x+nums[i-1]] += a[i-1][x]
                a[i][x-nums[i-1]] += a[i-1][x]
        print(a)
        return a[-1][target]