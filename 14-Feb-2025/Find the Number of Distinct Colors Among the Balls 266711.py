# Problem: Find the Number of Distinct Colors Among the Balls - https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description/

from collections import defaultdict
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        D = defaultdict(int)
        colors = defaultdict(int)
        nbColors = 0
        res = []
        for q in queries:
            if colors[q[0]] != 0:
                D[colors[q[0]]] -= 1
                if D[colors[q[0]]] == 0:
                    nbColors -= 1
            colors[q[0]] = q[1]
            D[q[1]] += 1
            if D[q[1]] == 1:
                nbColors += 1
            res.append(nbColors)
        return res