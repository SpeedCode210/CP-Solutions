# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

from collections import deque
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n = len(isWater)
        m = len(isWater[0])
        D = deque()
        for i in range(n):
            for j in range(m):
                isWater[i][j] = 1 - isWater[i][j]
                if isWater[i][j] == 0:
                    D.append((i,j))
        
        while len(D):
            d = D[0]
            D.popleft()
            for x in [(d[0], d[1]+1), (d[0], d[1]-1), (d[0]-1, d[1]), (d[0]+1, d[1])]:
                if x[0] < 0 or x[1] < 0 or x[0] >= n or x[1] >= m:
                    continue
                
                if isWater[x[0]][x[1]] > 0:
                    isWater[x[0]][x[1]] = isWater[d[0]][d[1]] - 1
                    D.append((x[0], x[1]))

        for i in range(n):
            for j in range(m):
                isWater[i][j] *= -1
        return isWater