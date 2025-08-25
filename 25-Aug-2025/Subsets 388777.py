# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(1<<len(nums)):
            k = []
            for j in range(len(nums)):
                if (1<<j)&i:
                    k.append(nums[j])
            res.append(k)
        return res