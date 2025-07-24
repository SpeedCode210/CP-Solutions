# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

from collections import deque
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        G = [[] for i in range(n)]
        for i in range(n):
            for x in graph[i]:
                G[x].append(i)
        graph = G
        gud = [False]*n
        indegs = [0]*n
        for i in range(n):
            for x in graph[i]:
                indegs[x] += 1
        res = []
        d = deque([x for x in range(n) if indegs[x] == 0])
        while len(d):
            x = d[0]
            d.popleft()
            gud[x] = True
            res.append(x)
            for y in graph[x]:
                indegs[y] -= 1
                if indegs[y] == 0:
                    d.append(y)


        return [i for i in range(n) if gud[i]]