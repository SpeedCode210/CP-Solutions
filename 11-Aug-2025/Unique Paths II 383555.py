# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        res = [[0]*n for i in range(m)]
        res[0][0] = 1 - obstacleGrid[0][0]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    continue
                if i > 0 and obstacleGrid[i-1][j] == 0:
                    res[i][j] += res[i-1][j]
                if j > 0 and obstacleGrid[i][j-1] == 0:
                    res[i][j] += res[i][j-1]
        return res[-1][-1]