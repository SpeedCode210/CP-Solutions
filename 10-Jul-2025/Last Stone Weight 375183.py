# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            a, b = heapq.heappop(stones), heapq.heappop(stones)
            if a != b:
                heapq.heappush(stones, a-b)
        return -stones[0] if len(stones) else 0
