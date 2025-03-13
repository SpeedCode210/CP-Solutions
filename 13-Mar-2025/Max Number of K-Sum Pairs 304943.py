# Problem: Max Number of K-Sum Pairs - https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        p1 = 0
        p2 = len(nums)-1
        res = 0
        while p1 < p2:
            s = nums[p1]+nums[p2]
            if s < k:
                p1 += 1
            elif s > k:
                p2 -= 1
            else:
                res += 1
                p1 += 1
                p2 -= 1
        return res