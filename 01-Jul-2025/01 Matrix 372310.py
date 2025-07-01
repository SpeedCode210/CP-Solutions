# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        vis = [[-1 for i in range(m)] for j in range(n)]
        d = deque()
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    d.appendleft((i,j))
                    vis[i][j] = 0
        while len(d):
            p = d[-1]
            d.pop()

            for c in [(0,1),(1,0),(-1,0),(0,-1)]:
                if n > p[0]+c[0] >= 0 and m > p[1]+c[1] >= 0 and vis[p[0]+c[0]][p[1]+c[1]] == -1:
                    vis[p[0]+c[0]][p[1]+c[1]] = vis[p[0]][p[1]] + 1
                    d.appendleft((p[0]+c[0],p[1]+c[1]))
        return vis