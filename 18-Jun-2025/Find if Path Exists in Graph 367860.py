# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for i in range(n)]
        for c in edges:
            graph[c[0]].append(c[1])
            graph[c[1]].append(c[0])

        visited = [0]*n

        def dfs(node):
            for child in graph[node]:
                if visited[child] == 0:
                    visited[child] = 1
                    dfs(child)

        visited[source] = 1        
        dfs(source)
        return visited[destination] == 1

