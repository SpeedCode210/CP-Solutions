# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        outdeg = [0]*(n+1)
        indeg = [0]*(n+1)
        for a in trust:
            outdeg[a[0]] += 1
            indeg[a[1]] += 1
        for i in range(1, n+1):
            if outdeg[i] == 0 and indeg[i] == n-1:
                return i
        return -1