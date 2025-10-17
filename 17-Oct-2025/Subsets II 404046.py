# Problem: Subsets II - https://leetcode.com/problems/subsets-ii/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(2**len(nums)):
            skip = False
            for j in range(1, len(nums)):
                if nums[j] == nums[j-1] and (i>>j)%2 ==1 and (i >>(j-1))%2 == 0:
                    skip = True
            if not skip:
                res.append([nums[j] for j in range(len(nums)) if (i>>j)%2])
        return res