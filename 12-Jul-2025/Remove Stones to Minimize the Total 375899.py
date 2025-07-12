# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

from heapq import heapify , heappush, heappop
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        a = [-x for x in piles]
        heapify(a)

        i = 0
        while i < k and len(a) > 0:
            i += 1
            x = a[0]
            heappop(a)
            heappush(a, -((-x) - (-x)//2))
        return -sum(a)