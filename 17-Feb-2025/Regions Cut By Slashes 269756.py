# Problem: Regions Cut By Slashes - https://leetcode.com/problems/regions-cut-by-slashes/description/


from collections import deque
from collections import defaultdict
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        graph = defaultdict(lambda : [])
        group = defaultdict(int)
        for i in range(0, len(grid) - 1):
            for j in range(0, len(grid[0])):
                graph[(i,j,2)].append((i+1,j,4))
                graph[(i+1,j,4)].append((i,j,2))
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0]) - 1):
                graph[(i,j+1,1)].append((i,j,3))
                graph[(i,j,3)].append((i,j+1,1))

        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == " ":
                    graph[(i,j,1)].append((i,j,2))
                    graph[(i,j,2)].append((i,j,3))
                    graph[(i,j,3)].append((i,j,4))
                    graph[(i,j,4)].append((i,j,1))
                    graph[(i,j,2)].append((i,j,1))
                    graph[(i,j,3)].append((i,j,2))
                    graph[(i,j,4)].append((i,j,3))
                    graph[(i,j,1)].append((i,j,4))
                elif grid[i][j] == "/":
                    graph[(i,j,2)].append((i,j,3))
                    graph[(i,j,4)].append((i,j,1))
                    graph[(i,j,3)].append((i,j,2))
                    graph[(i,j,1)].append((i,j,4))
                elif grid[i][j] == "\\":
                    graph[(i,j,1)].append((i,j,2))
                    graph[(i,j,3)].append((i,j,4))
                    graph[(i,j,2)].append((i,j,1))
                    graph[(i,j,4)].append((i,j,3))
        nb = 0
        for vertex in graph:
            if group[vertex] != 0:
                continue
            nb += 1
            group[vertex] = nb
            bfs = deque()
            bfs.append(vertex)
            while len(bfs) > 0:
                v = bfs.popleft()
                for x in graph[v]:
                    if group[x] != 0:
                        continue
                    group[x] = nb
                    bfs.append(x)
        
        return nb

            

        