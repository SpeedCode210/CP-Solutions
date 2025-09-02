# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        roads.sort(key=  lambda x : x[2])

        uf = [i for i in range(n+1)]
        h = [1000000000]*(n+1)
        def f(x):
            h = []
            while x != uf[x]:
                h.append(x)
                x = uf[x]
            for i in h:
                uf[i] = x
            return x

        for r in roads:
            if f(r[0]) != f(r[1]):
                h[f(r[1])] = min(h[f(r[0])], h[f(r[1])], r[2])
                uf[f(r[0])] = f(r[1])

        return h[f(1)]