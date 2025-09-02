# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        queries = [x + [i] for i, x in enumerate(queries)]

        queries.sort(key=lambda x : x[2])
        edgeList.sort(key = lambda x : x[2])

        p = 0

        uf = [i for i in range(n)]

        def f(x):
            h = []
            while x != uf[x]:
                h.append(x)
                x = uf[x]
            for i in h:
                uf[i] = x
            return x

        res = [False]*len(queries)

        for q in queries:
            while p < len(edgeList) and edgeList[p][2] < q[2]:
                if f(edgeList[p][0]) != f(edgeList[p][1]):
                    uf[f(edgeList[p][0])] = f(edgeList[p][1])
                p += 1
            if f(q[0]) == f(q[1]):
                res[q[3]] = True

        return res