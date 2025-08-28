# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        group = {}
        def get_grp(s):
            if s not in group:
                group[s] = s
                return s
            h = []
            while group[s] != s:
                h.append(s)
                s = group[s]
            for x in h:
                group[x] = s
            return s

        for x in edges:
            if get_grp(x[0]) == get_grp(x[1]):
                return x
            group[get_grp(x[0])] = get_grp(x[1])