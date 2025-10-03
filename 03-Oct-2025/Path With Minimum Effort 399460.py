# Problem: Path With Minimum Effort - https://leetcode.com/problems/path-with-minimum-effort/description/

from heapq import heappush, heappop
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n = len(heights)
        m = len(heights[0])
        vu = [[False]*m for _ in range(n)]
        d = [[1000000000]*m for _ in range(n)]
        d[0][0] = 0
        heap = [(0,0,0)]
        while len(heap):
            _d,x,y = heap[0]
            heappop(heap)
            if vu[x][y]:
                continue
            vu[x][y] = True

            for a,b in [(x,y+1), (x,y-1), (x+1, y), (x-1, y)]:
                if 0 <= a < n and 0 <= b < m:
                    D = max(_d, abs(heights[x][y] - heights[a][b]))
                    if D < d[a][b]:
                        heappush(heap, (D,a,b))
                        d[a][b] = D


        return d[n-1][m-1]
    