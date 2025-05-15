# Problem: Next Greater Element II - https://leetcode.com/problems/next-greater-element-ii/

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1]*len(nums)
        stack = []
        for I in range(2*len(nums)):
            i = I%len(nums)
            while len(stack) > 0 and nums[stack[-1]] < nums[i]:
                res[stack[-1]] = nums[i]
                stack.pop()
            if res[i] == -1:
                stack.append(i)

        return res