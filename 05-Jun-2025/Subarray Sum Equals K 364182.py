# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        D = defaultdict(int)
        D[0] = 1
        somme = 0
        res = 0
        for c in nums:
            somme += c
            res += D[somme - k]
            D[somme] += 1
        return res