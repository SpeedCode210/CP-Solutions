# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = numCourses
        indegs = [0]*n
        graph = [[] for i in range(n)]
        for x in prerequisites:
            indegs[x[0]] += 1
            graph[x[1]].append(x[0])
        
        bfs = deque([x for x in range(n) if indegs[x] == 0])
        res = []
        while len(bfs):
            x = bfs[0]
            res.append(x)
            bfs.popleft()
            for y in graph[x]:
                indegs[y] -= 1
                if indegs[y] == 0:
                    bfs.append(y)
                    
        return res if len(res) == n else []
