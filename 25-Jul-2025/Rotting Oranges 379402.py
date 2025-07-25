# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        bfs = deque()
        dist = [[1000000000]*n for i in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    dist[i][j] = 0
                    bfs.append((i,j))
        res = 0
        while len(bfs):
            x = bfs[0]
            res = max(res, dist[x[0]][x[1]])
            bfs.popleft()

            for y in [(x[0]+1, x[1]+0),(x[0]-1, x[1]+0), (x[0]+0, x[1]+1), (x[0]+0, x[1]-1)]:
                if y[0] in [-1, m] or y[1] in [-1,n] or grid[y[0]][y[1]] == 0 or dist[y[0]][y[1]] != 1000000000:
                    continue
                dist[y[0]][y[1]] = 1 + dist[x[0]][x[1]]
                bfs.append(y)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and dist[i][j] == 1000000000:
                    return -1

        return res
