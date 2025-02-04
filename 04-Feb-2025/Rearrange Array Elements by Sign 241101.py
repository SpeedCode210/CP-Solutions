# Problem: Rearrange Array Elements by Sign - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        negative = [x for x in nums if x < 0]
        positive = [x for x in nums if x > 0]
        result = []
        for i in range(len(negative)):
            result.append(positive[i])
            result.append(negative[i])
        return result