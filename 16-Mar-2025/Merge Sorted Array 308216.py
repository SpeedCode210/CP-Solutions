# Problem: Merge Sorted Array - https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p0,p1 = m-1,n-1
        for i in range(n+m-1, -1, -1):
            if p0 == -1:
                nums1[i] = nums2[p1]
                p1 -= 1
            elif p1 == -1 or nums1[p0] > nums2[p1]:
                nums1[i] = nums1[p0]
                p0 -= 1
            else:
                nums1[i] = nums2[p1]
                p1 -= 1