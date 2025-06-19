# Problem: Course Schedule - https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for i in range(numCourses)]
        visited = [0]*numCourses

        for x in prerequisites:
            graph[x[1]].append(x[0])

        def dfs(node):
            visited[node] = 1
            for child in graph[node]:
                if visited[child] == 1:
                    return False
                if visited[child] == 0:
                    if not dfs(child):
                        return False
            visited[node] = 2
            return True
        
        for i in range(numCourses):
            if visited[i] == 0:
                if not dfs(i):
                    return False
        return True