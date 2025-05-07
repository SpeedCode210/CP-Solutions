# Problem: Search in Rotated Sorted Array - https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        bound = nums[0]
        a = 0
        b = len(nums) - 1
        while a < b:
            m = (a+b)//2
            if nums[m] < bound:
                b = m 
            else:
                a = m+1
        
        X = a

        a = 0
        b = X - 1

        while a <= b:
            m = (a+b+1)//2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                a = m+1
            else:
                b = m-1

        a = X
        b = len(nums)-1

        while a <= b:
            m = (a+b+1)//2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                a = m+1
            else:
                b = m-1
                
        return -1