# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        nums = [x for x in set(nums)]
        nums.sort()
        
        if len(nums) == 1:
            return 0

        def call(bit, l1, r1, l2, r2):
            if bit == -1:
                return 0
            res = 0
            # 10
            if (nums[r1]&(1<<bit)) and 0 == (nums[l2]&(1<<bit)):
                for i in range(l1, r1+1):
                    if (nums[i]&(1<<bit)):
                        for j in range(r2, l2-1, -1):
                            if 0 == (nums[j]&(1<<bit)):
                                res = call(bit-1, i, r1, l2, j) + (1<<bit)
                                break
                        break
            # 01
            if (nums[r2]&(1<<bit)) and 0 == (nums[l1]&(1<<bit)):
                for i in range(l2, r2+1):
                    if (nums[i]&(1<<bit)):
                        for j in range(r1, l1-1, -1):
                            if 0 == (nums[j]&(1<<bit)):
                                res = max(res, call(bit-1, i, r2, l1, j) + (1<<bit))
                                break
                        break
            # otherwise
            if res == 0:
                return call(bit-1, l1, r1, l2, r2)
            else :
                return res
            

        for bit in range(32,-1,-1):
            if (nums[-1]&(1<<bit)) != (nums[0]&(1<<bit)):
                for i in range(len(nums)):
                    if (nums[i]&(1<<bit)):
                        return (1<<bit) + call(bit-1, 0, i-1, i, len(nums)-1)