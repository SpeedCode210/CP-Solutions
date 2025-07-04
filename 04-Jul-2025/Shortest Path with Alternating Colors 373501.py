# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

from collections import deque
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        redGraph = [[] for i in range(n)]
        blueGraph = [[] for i in range(n)]

        for x in redEdges:
            redGraph[x[0]].append(x[1])

        for x in blueEdges:
            blueGraph[x[0]].append(x[1])

        
        res = [[1000000000 for i in range(n)] for j in range(2)]

        bfs = deque()
        bfs.append((0,0))
        bfs.append((0,1))

        res[0][0] = 0
        res[1][0] = 0

        while len(bfs):
            a = bfs[0]
            bfs.popleft()

            for x in (redGraph if a[1] else blueGraph)[a[0]]:
                if res[1-a[1]][x] == 1000000000:
                    bfs.append((x, 1-a[1]))
                    res[1-a[1]][x] = res[a[1]][a[0]] + 1
        
        return [min(res[1][i], res[0][i]) if min(res[1][i], res[0][i]) != 1000000000 else -1 for i in range(n)]

            