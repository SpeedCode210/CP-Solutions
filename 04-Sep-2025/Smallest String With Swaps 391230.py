# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

from heapq import heappush, heappop
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        uf = [i for i in range(len(s))]

        def g(x):
            h=  []
            while x != uf[x]:
                h.append(x)
                x=  uf[x]
            for i in h :
                uf[i] = x
            return x
        
        for x,y in pairs:
            if g(x) != g(y):
                uf[g(x)] = g(y)

        res = [[] for i in range(len(s))]

        for i in range(len(s)):
            heappush(res[g(i)], s[i])

        Res = []
        for i in range(len(s)):
            Res.append(res[g(i)][0])
            heappop(res[g(i)])

        return "".join(Res)