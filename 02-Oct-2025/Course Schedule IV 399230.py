# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        d = [[1]*numCourses for _ in range(numCourses)]

        for x in prerequisites:
            d[x[0]][x[1]] = 0

        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    d[i][j] = min(d[i][j], d[i][k]+d[k][j])
        
        return [0 == d[i][j] for i,j in queries]