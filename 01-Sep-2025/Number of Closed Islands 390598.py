# Problem: Number of Closed Islands - https://leetcode.com/problems/number-of-closed-islands/

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        def fill(i, j):
            dfs = [(i,j)]
            grid[i][j] = 1
            while len(dfs):
                x = dfs[-1]
                dfs.pop()
                for u in [(x[0], x[1]+1), (x[0], x[1]-1), (x[0]+1, x[1]), (x[0]-1, x[1])]:
                    if u[0] < 0 or u[1] < 0 or u[0] >= n or u[1] >= m or grid[u[0]][u[1]]:
                        continue
                    grid[u[0]][u[1]] = 1
                    dfs.append(u)
            
        for i in range(n):
            if 0 == grid[i][0]:
                fill(i,0)
            if 0 == grid[i][m-1]:
                fill(i,m-1)
        for i in range(m):
            if 0 == grid[0][i]:
                fill(0,i)
            if 0 == grid[n-1][i]:
                fill(n-1,i)
                    
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    res += 1
                    fill(i,j)

        return res