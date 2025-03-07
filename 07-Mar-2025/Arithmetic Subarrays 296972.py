# Problem: Arithmetic Subarrays - https://leetcode.com/problems/arithmetic-subarrays/

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        return [len(set([sorted(nums[l[i]:r[i]+1])[j+1] - sorted(nums[l[i]:r[i]+1])[j] for j in range(r[i]-l[i])])) == 1 for i in range(len(l))]