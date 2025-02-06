# Problem: Tuple with Same Product - http://leetcode.com/problems/tuple-with-same-product

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        hi = dict([(0,0)])
        for i in range(len(nums)):
            for j in range(i):
                x = nums[i]*nums[j]
                if x in hi:
                    hi[x] += 1
                else:
                    hi[x] = 1
        res = 0
        for key in hi:
            res += hi[key]*(hi[key]-1)*4
        return res