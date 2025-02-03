# Problem: Bitwise XOR of All Pairings - https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/?envType=problem-list-v2&envId=brainteaser

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        if len(nums1)%2 == 1:
            for c in nums2:
                res = res ^ c
        if len(nums2)%2 == 1:
            for c in nums1:
                res = res ^ c
        return res