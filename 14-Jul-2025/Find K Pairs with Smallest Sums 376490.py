# Problem: Find K Pairs with Smallest Sums - https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/

from heapq import heappop, heappush
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []

        for i in range(len(nums1)):
            for j in range(i, len(nums2)):
                x = (-nums1[i]-nums2[j], nums1[i], nums2[j])
                heappush(heap, x)
                if len(heap) == k+1:
                    if heap[0] == x:
                        heappop(heap)
                        break
                    heappop(heap)

        for i in range(len(nums2)):
            for j in range(i+1, len(nums1)):
                x = (-nums1[j]-nums2[i], nums1[j], nums2[i])
                heappush(heap, x)
                if len(heap) == k+1:
                    if heap[0] == x:
                        heappop(heap)
                        break
                    heappop(heap)
            
        return [[x[1], x[2]] for x in heap]