# Problem: Concatenation of Array - https://leetcode.com/problems/concatenation-of-array/description/

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(0, 2*len(nums)):
            result.append(nums[i%len(nums)])

        return result