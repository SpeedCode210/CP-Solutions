# Problem: Count Servers that Communicate - https://leetcode.com/problems/count-servers-that-communicate/description/

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        a = [0]*n
        b = [0]*m

        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    a[i] += 1
                    b[j] += 1
        
        res = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] and (a[i] > 1 or b[j] > 1):
                    res += 1
        
        return res