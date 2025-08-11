# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        h = set([0])
        for x in nums:
            h = h.union([x+y for y in h])
        return sum(nums)%2 == 0 and sum(nums)//2 in h