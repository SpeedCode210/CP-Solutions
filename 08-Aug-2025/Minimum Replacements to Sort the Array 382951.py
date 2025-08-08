# Problem: Minimum Replacements to Sort the Array - https://leetcode.com/problems/minimum-replacements-to-sort-the-array/

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        nums = [x for x in reversed(nums)]
        last = nums[0]
        res = 0
        for x in nums:
            if x <= last:
                last = x
                continue
            nb = (x+last-1)//last
            res += nb-1
            last = x//nb
        return res