# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*(m+1) for i in range(n+1)]
        dp[1][1] = 1
        for i in range(1,1+n):
            for j in range(1, 1+m):
                if i == j == 1:
                    continue
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[n][m]