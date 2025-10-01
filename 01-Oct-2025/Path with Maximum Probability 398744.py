# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

from heapq import heappush, heappop
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        res = [0]*n
        visited = [False]*n
        queue = [(-1, start_node)]

        res[start_node] = 1

        graph = [[] for i in range(n)]

        for i in range(len(edges)):
            graph[edges[i][0]].append([edges[i][1], succProb[i]])
            graph[edges[i][1]].append([edges[i][0], succProb[i]])
        
        while len(queue):
            a = queue[0]
            heappop(queue)
            if visited[a[1]]:
                continue

            visited[a[1]] = True

            for e in graph[a[1]]:
                if res[a[1]]*e[1] > res[e[0]]:
                    res[e[0]] = res[a[1]]*e[1]
                    heappush(queue, (-res[e[0]], e[0]))

        return res[end_node]