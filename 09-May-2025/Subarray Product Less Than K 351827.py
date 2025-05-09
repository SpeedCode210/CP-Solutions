# Problem: Subarray Product Less Than K - https://leetcode.com/problems/subarray-product-less-than-k/

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        p1 = 0
        prod = 1
        res = 0
        for i in range(len(nums)):
            prod *= nums[i]
            while prod >= k and p1 < i:
                prod /= nums[p1]
                p1 += 1
            if nums[i] < k:
                res += i-p1+1
        return res
