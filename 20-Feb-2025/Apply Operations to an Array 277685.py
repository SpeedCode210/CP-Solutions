# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i = 0
        res = []
        nums.append(0)
        while(i < len(nums)-1):
            if nums[i] == nums[i+1] and nums[i] != 0:
                nums[i] *= 2
                nums[i+1] = 0
                res.append(nums[i])
                i += 1
            elif nums[i] != 0:
                res.append(nums[i])
            i += 1
        while len(res) < len(nums)-1:
            res.append(0)
        return res

