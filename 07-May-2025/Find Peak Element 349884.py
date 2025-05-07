# Problem: Find Peak Element - https://leetcode.com/problems/find-peak-element

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        a = 0
        b = len(nums)-1

        def f(i):
            if i >= 0 and i < len(nums):
                return nums[i]
            return -3000000000

        while a <= b:
            m = (a+b+1)//2
            if f(m) > f(m-1) and f(m) > f(m+1):
                return m
            elif f(m) > f(m+1):
                b = m-1
            else:
                a = m+1