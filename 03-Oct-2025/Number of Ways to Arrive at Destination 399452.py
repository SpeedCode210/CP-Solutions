# Problem: Number of Ways to Arrive at Destination - https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/

from heapq import heappush, heappop
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        D = [1000000000000000000]*n
        w = [0]*n
        vu = [False]*n
        D[0] = 0
        w[0] = 1

        heap = [(0,0)]

        graph = [[] for _ in range(n)]
        for x,y,z in roads:
            graph[x].append((y, z))
            graph[y].append((x, z))

        while len(heap):
            d,a = heap[0]
            heappop(heap)
            if vu[a]:
                continue
            vu[a] = True
            for x, y in graph[a]:
                if d+y < D[x]:
                    D[x] = d+y
                    w[x] = 0
                    heappush(heap, (d+y, x))
                if d+y == D[x]:
                    w[x] += w[a]
                    w[x] %= 1000000007
        
        return w[n-1]