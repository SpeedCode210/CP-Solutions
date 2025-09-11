# Problem: Distinct Prime Factors of Product of Array - https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        spf = [1000000000]*(1001)
        spf[1] = 1
        for i in range(2, 1001):
            if spf[i] <= i:
                continue
            for j in range(i, 1001, i):
                spf[j] = min(spf[j], i)
        res = [0]*(1001)
        for x in nums:
            r = x
            while r != 1:
                res[spf[r]] = 1
                r //= spf[r]
        return sum(res)