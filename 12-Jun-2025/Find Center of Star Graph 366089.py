# Problem: Find Center of Star Graph - https://leetcode.com/problems/find-center-of-star-graph/

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        degs = [0]*len(edges*2)
        for x in edges:
            degs[x[0]] += 1
            degs[x[1]] += 1
            if degs[x[0]] > 1:
                return x[0]
            if degs[x[1]] > 1:
                return x[1]