# Problem: Minimum Number of Vertices to Reach All Nodes - https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        r = [0]*n
        for x in edges:
            r[x[1]] += 1
        return [x for x in range(n) if r[x] == 0]