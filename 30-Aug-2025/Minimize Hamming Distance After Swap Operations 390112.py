# Problem: Minimize Hamming Distance After Swap Operations - https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/description/

from collections import defaultdict
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        grps = [i for i in range(len(source))]
        sz = [1 for i in range(len(source))]

        def get_grp(n):
            hi = []
            while grps[n] != n:
                hi.append(n)
                n = grps[n]
            for x in hi:
                grps[x] = n
            return n
        
        for x in allowedSwaps:
            x[0] = get_grp(x[0])
            x[1] = get_grp(x[1])
            if sz[x[0]] == sz[x[1]]:
                grps[x[0]] = x[1]
                sz[x[1]] += 1
            elif sz[x[0]] < sz[x[1]]:
                grps[x[0]] = x[1]
            else:
                grps[x[1]] = x[0]
            
        
        dist = len(source)
        h = [[defaultdict(lambda : 0), defaultdict(lambda : 0)] for i in range(len(source))]
        for i in range(len(source)):
            h[get_grp(i)][0][source[i]] += 1
            h[get_grp(i)][1][target[i]] += 1
        for x in h:
            for y in x[0]:
                dist -= min(x[0][y], x[1][y])
        
        return dist