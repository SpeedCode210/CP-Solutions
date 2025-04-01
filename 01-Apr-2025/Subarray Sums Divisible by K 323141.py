# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

from collections import Counter
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        a = [0]
        for c in nums:
            a.append(((a[-1] + c)%k + k)%k)
        C = Counter(a)
        return sum([C[x]*(C[x]-1)//2 for x in C])