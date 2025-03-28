# Problem: Partition Array According to Given Pivot - https://leetcode.com/problems/partition-array-according-to-given-pivot/description/

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        res = [pivot]*len(nums)
        p = 0
        for c in nums:
            if c < pivot:
                res[p] = c
                p += 1
        nums.reverse()
        p = -1
        for c in nums:
            if c > pivot:
                res[p] = c
                p -= 1
        return res