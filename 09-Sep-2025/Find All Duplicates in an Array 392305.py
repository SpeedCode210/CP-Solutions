# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = [0]*(len(nums)+1)
        for i in nums:
            res[i] += 1
        return [i for i in range(len(nums)+1) if res[i]==2]