# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        res = [-1]*len(nums2)
        d = dict()
        for i in range(len(nums2)-1, -1, -1):
            while len(stack) > 0 and stack[-1] < nums2[i]:
                stack.pop()
            if len(stack) > 0:
                res[i] = stack[-1]
            d[nums2[i]] = res[i]
            stack.append(nums2[i])
        return [d[nums1[i]] for i in range(len(nums1))]