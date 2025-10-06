# Problem: Minimum Cost to Make at Least One Valid Path in a Grid - https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/description/?envType=problem-list-v2&envId=shortest-path

from collections import deque
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        
        distances = [[1000000000]*len(grid[0]) for _ in range(len(grid))]
        flags = [[0]*len(grid[0]) for _ in range(len(grid))]
        distances[0][0] = 0
        bfs = deque()
        bfs.append((0,0))
        directions = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]
        while len(bfs):
            node = bfs[-1]
            bfs.pop()
            for i in range(1, 5):
                c = (node[0] + directions[i][0], node[1] + directions[i][1])
                if c[0] < 0 or c[1] < 0:
                    continue
                if c[0] >= len(grid) or c[1] >= len(grid[0]):
                    continue
                if i == grid[node[0]][node[1]]:
                
                    distances[c[0]][c[1]] = min(distances[node[0]][node[1]], distances[c[0]][c[1]])
                    if (0 == (flags[c[0]][c[1]] % 2)):
                    
                        bfs.append(c)
                        flags[c[0]][c[1]] |= 1
                       
                else:   
                    distances[c[0]][c[1]] = min(distances[c[0]][c[1]], 1 + distances[node[0]][node[1]])
                    if (0 == ((flags[c[0]][c[1]]/2) % 2)):
                        bfs.appendleft(c)
                        flags[c[0]][c[1]] |= 2
                    

        return distances[-1][-1]
