# Problem: Kth Smallest Element in a Sorted Matrix - https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

from heapq import heappop, heappush
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heappush(heap, -matrix[i][j])
                while len(heap) > k:
                    heappop(heap)

        return -heap[0]