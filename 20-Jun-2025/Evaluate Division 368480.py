# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(lambda : [])

        for i in range(len(values)):
            graph[equations[i][0]].append((equations[i][1], values[i]))
            graph[equations[i][1]].append((equations[i][0], 1/values[i]))
        
        res = []
        for q in queries:
            visited = defaultdict(lambda : False)
            def dfs(current, target):
                if current not in graph:
                    return None
                visited[current] = True
                if current == target:
                    return 1.0

                for c in graph[current]:
                    if visited[c[0]]:
                        continue
                    visited[c[0]] = True
                    x = dfs(c[0], target)
                    if x is not None:
                        return x*c[1]

                return None

            visited[q[0]] = True
            X = dfs(q[0], q[1])

            res.append(-1 if X is None else X)

        return res
from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(lambda : [])

        for i in range(len(values)):
            graph[equations[i][0]].append((equations[i][1], values[i]))
            graph[equations[i][1]].append((equations[i][0], 1/values[i]))
        
        res = []
        for q in queries:
            visited = defaultdict(lambda : False)
            def dfs(current, target):
                if current not in graph:
                    return None
                visited[current] = True
                if current == target:
                    return 1.0

                for c in graph[current]:
                    if visited[c[0]]:
                        continue
                    visited[c[0]] = True
                    x = dfs(c[0], target)
                    if x is not None:
                        return x*c[1]

                return None

            visited[q[0]] = True
            X = dfs(q[0], q[1])

            res.append(-1 if X is None else X)

        return res
