# Problem: Find a Safe Walk Through a Grid - https://leetcode.com/problems/find-a-safe-walk-through-a-grid/description/?envType=problem-list-v2&envId=shortest-path

from heapq import heappush, heappop

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        heap = [(-health + grid[0][0], 0, 0)]
        h = [[-1000000000000000]*(len(grid[0])) for _ in range(len(grid))]
        V = [[False]*(len(grid[0])) for _ in range(len(grid))]
        h[0][0] = health - grid[0][0]
        while len(heap):
            d,x,y = heap[0]
            heappop(heap)
            if V[x][y] or d == 0:
                continue
            V[x][y] = True

            for u,v in [(x,y+1),(x,y-1),(x-1,y),(x+1,y)]:
                if 0 <= u < len(grid) and 0 <= v < len(grid[0]):
                    if h[u][v] < -d - grid[u][v] and 0 < -d - grid[u][v]:
                        h[u][v] = -d - grid[u][v]
                        heappush(heap, (-h[u][v],u,v))
        
        return V[-1][-1]
