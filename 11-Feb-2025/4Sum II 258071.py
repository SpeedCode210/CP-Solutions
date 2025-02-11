# Problem: 4Sum II - https://leetcode.com/problems/4sum-ii/

from collections import defaultdict
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        D = defaultdict(int)
        D2 = defaultdict(int)
        for n in nums1:
            D[n] += 1
        
        for n in nums2:
            for x in D:
                D2[n+x] += D[x]
        D = D2
        D2 = defaultdict(int)

        for n in nums3:
            for x in D:
                D2[n+x] += D[x]

        D = D2
        D2 = defaultdict(int)

        for n in nums4:
            for x in D:
                D2[n+x] += D[x]
        
        return D2[0]
