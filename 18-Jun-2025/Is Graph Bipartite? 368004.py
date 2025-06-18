# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [0]*n
        
        def check(node):
            if colors[node] == 0:
                colors[node] = 1

            for x in graph[node]:
                if colors[x] == colors[node]:
                    return False
                if colors[x] != 0:
                    continue
                colors[x] = 2 if colors[node] == 1 else 1
                if not check(x):
                    return False
            return True

        for x in range(n):
            if colors[x] == 0:
                if not check(x):
                    return False
        return True
            