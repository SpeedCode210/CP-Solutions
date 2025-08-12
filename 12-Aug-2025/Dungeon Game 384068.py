# Problem: Dungeon Game - https://leetcode.com/problems/dungeon-game/

from collections import defaultdict
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n = len(dungeon)
        m = len(dungeon[0])
        a = 1
        b = 40000000

        def can(health):
            dp = [[0]*m for i in range(n)]

            dp[0][0] = dungeon[0][0] + health

            if dp[0][0] <= 0 :
                return False

            for i in range(n):
                for j in range(m):
                    if i == 0 == j:
                        continue
                    if i > 0 and dp[i-1][j] > 0:
                        dp[i][j] = max(dp[i][j], dp[i-1][j] + dungeon[i][j])
                    if j > 0 and dp[i][j-1] > 0:
                        dp[i][j] = max(dp[i][j], dp[i][j-1] + dungeon[i][j])

            return dp[-1][-1] > 0

        while a < b:
            M = (a+b)//2
            if can(M):
                b = M
            else:
                a = M+1

        return a