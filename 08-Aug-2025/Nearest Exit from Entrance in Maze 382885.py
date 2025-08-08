# Problem: Nearest Exit from Entrance in Maze - https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        bfs = deque([entrance])
        res = [[-1 for j in range(len(maze[0]))] for i in range(len(maze))]
        res[entrance[0]][entrance[1]] = 0

        while len(bfs):
            x = bfs[0]
            bfs.popleft()
            for y in [ [x[0]+(+1), x[1]+(0)], [x[0]+(-1), x[1]+(0)], [x[0]+(0), x[1]+(1)], [x[0]+(0), x[1]+(-1)] ]:
                if y[0] < 0 or y[1] < 0 or y[0] == len(maze) or y[1] == len(maze[0]):
                    if res[x[0]][x[1]] == 0:
                        continue
                    return res[x[0]][x[1]]
                if maze[y[0]][y[1]] == '+':
                    continue
                if res[y[0]][y[1]] != -1:
                    continue
                res[y[0]][y[1]] = res[x[0]][x[1]]+1
                bfs.append(y)
                
        return -1
