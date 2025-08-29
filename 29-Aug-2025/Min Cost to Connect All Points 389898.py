# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

from collections import defaultdict
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        hi = [i for i in range(len(points))]
        sz = [1 for i in range(len(points))]
        def g(i):
            st = []
            while i != hi[i]:
                st.append(i)
                i = hi[i]
            for x in st:
                hi[x] = i
            return i
        
        edges = []

        for i in range(len(points)):
            for j in range(i):
                edges.append((abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1]),i,j))

        edges.sort()
        res = 0
        for x in edges:
            i,x,y = x
            x = g(x)
            y = g(y)
            if x == y:
                continue

            if sz[x] == sz[y]:
                hi[x] = y
                sz[x] += 1
            elif sz[x] < sz[y]:
                hi[x] = y
            else:
                hi[y] = x

            res += i
        return res