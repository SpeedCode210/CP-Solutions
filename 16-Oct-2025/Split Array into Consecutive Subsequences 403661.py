# Problem: Split Array into Consecutive Subsequences - https://leetcode.com/problems/split-array-into-consecutive-subsequences/

from heapq import heappush, heappop
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        heaps = defaultdict(lambda : [])

        for x in nums:
            if len(heaps[x-1]):
                i = heaps[x-1][0]
                heappop(heaps[x-1])
                heappush(heaps[x], i+1)
            else:
                heappush(heaps[x], 1)
        
        return min([heaps[x][0] for x in heaps if len(heaps[x])]) >= 3
        
 