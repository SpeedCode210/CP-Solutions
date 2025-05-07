# Problem: Find the Smallest Divisor Given a Threshold - https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        a = 1
        b = sum(nums)

        while a < b:
            m = (a+b)//2
            X = sum([(c+m-1)//m for c in nums])
            if X <= threshold:
                b = m
            else:
                a = m+1
        return a