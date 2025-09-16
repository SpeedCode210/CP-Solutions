# Problem: Number of Subarrays With LCM Equal to K - https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/description/?envType=problem-list-v2&envId=number-theory

class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        def gcd(a,b):
            if max(a,b)%min(a,b) == 0:
                return min(a,b)
            return gcd(a%b,b%a)
        def lcm(a,b):
            return a*b//gcd(a,b)
        res = 0
        for i in range(len(nums)):
            l = 1
            for j in range(i, len(nums)):
                l = lcm(l, nums[j])
                if l == k:
                    res += 1
        return res
        