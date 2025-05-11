# Problem: Intersection of Two Arrays II - https://leetcode.com/problems/intersection-of-two-arrays-ii/

from collections import defaultdict
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = defaultdict(int)
        b = defaultdict(int)
        for c in nums1:
            a[c] += 1
        for c in nums2:
            b[c] += 1
        res = []
        for x in a:
            for i in range(min(a[x], b[x])):
                res.append(x)

        return res