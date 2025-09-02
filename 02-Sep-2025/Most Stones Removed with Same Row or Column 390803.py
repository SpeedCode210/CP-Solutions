# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

from collections import Counter
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        stones = [x + [i] for i,x in enumerate(stones)]
        uf = [i for i in range(len(stones))]
        
        def f(x):
            h = []
            while x != uf[x]:
                h.append(x)
                x = uf[x]
            for i in h:
                uf[i] = x
            return x
            
        stones.sort(key = lambda x : x[0])
        for i in range(1,len(stones)):
                if f(stones[i][2]) != f(stones[i-1][2]) and stones[i][0] == stones[i-1][0]:
                    uf[f(stones[i][2])] = f(stones[i-1][2])

        stones.sort(key=lambda x: x[1])

        for i in range(1,len(stones)):
                if f(stones[i][2]) != f(stones[i-1][2]) and stones[i][1] == stones[i-1][1]:
                    uf[f(stones[i][2])] = f(stones[i-1][2])
        
        C = Counter([f(i) for i in range(len(stones))])
        return sum([C[x]-1 for x in C])