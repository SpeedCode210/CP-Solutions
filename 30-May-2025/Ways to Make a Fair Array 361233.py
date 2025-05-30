# Problem: Ways to Make a Fair Array - https://leetcode.com/problems/ways-to-make-a-fair-array/description/

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        leftEven = 0
        leftOdd = 0
        rightEven = sum([nums[i] for i in range(0,len(nums), 2)])
        rightOdd = sum([nums[i] for i in range(1,len(nums), 2)])
        res = 0
        for i in range(len(nums)):
            if i%2 == 0:
                rightEven -= nums[i]
            else:
                rightOdd -= nums[i]

            if leftEven + rightOdd == leftOdd + rightEven:
                res += 1

            if i%2 == 0:
                leftEven += nums[i]
            else:
                leftOdd += nums[i]
            
        return res
