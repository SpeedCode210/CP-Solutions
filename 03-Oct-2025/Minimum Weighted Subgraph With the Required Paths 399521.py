# Problem: Minimum Weighted Subgraph With the Required Paths - https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/

from heapq import heappush, heappop
class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        graph = [[] for _ in range(n)]
        comp = [[] for _ in range(n)]
        for x,y,z in edges:
            graph[x].append((y, z))
            comp[y].append((x, z))

        d1 = [1000000000000]*n
        b1 = [False]*n
        d1[src1] = 0

        heap = [(0,src1)]
        while len(heap):
            d,a = heap[0]
            heappop(heap)
            if b1[a]:
                continue
            b1[a] = True
            for x, _d in graph[a]:
                if d + _d < d1[x]:
                    d1[x] = d+_d
                    heappush(heap, (d+_d, x))

        d2 = [1000000000000]*n
        d2[src2] = 0
        b2 = [False]*n

        heap = [(0,src2)]
        while len(heap):
            d,a = heap[0]
            heappop(heap)
            if b2[a]:
                continue
            b2[a] = True
            for x, _d in graph[a]:
                if d + _d < d2[x]:
                    d2[x] = d+_d
                    heappush(heap, (d+_d, x))

    
        d3 = [1000000000000]*n
        d3[dest] = 0
        b3 = [False]*n

        heap = [(0,dest)]
        while len(heap):
            d,a = heap[0]
            heappop(heap)
            if b3[a]:
                continue
            b3[a] = True
            for x, _d in comp[a]:
                if d + _d < d3[x]:
                    d3[x] = d+_d
                    heappush(heap, (d+_d, x))

        res = 1000000000000000

        for i in range(n):
            res = min(res, d1[i]+d2[i]+d3[i])
        
        return -1 if res > 100000000000 else res
        