# Problem: Maximum Width Ramp - https://leetcode.com/problems/maximum-width-ramp

class Solution:
    def maxWidthRamp(self, nums: list[int]) -> int:
        arr1 = [nums[0]]
        arr2 = [0]
        maxi = 0
        for i in range(1,len(nums)):
            if nums[i] < arr1[-1]:
                arr1.append(nums[i])
                arr2.append(i)
            else:
                # binary search the first smaller
                a = 0
                b = len(arr1)
                while b-a > 1:
                    mid = (a+b)//2
                    if arr1[mid-1] <= nums[i]:
                        b = mid
                    else:
                        a = mid
                maxi = max(i-arr2[a], maxi)
        return maxi
