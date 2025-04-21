# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a = [1]
        b = [1]
        for i in range(len(nums)):
            a.append(a[-1]*nums[i])
            b.append(b[-1]*nums[-i-1])

        return [a[i]*b[-i-2] for i in range(len(nums))]