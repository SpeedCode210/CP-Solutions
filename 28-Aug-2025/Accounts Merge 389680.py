# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        groups = defaultdict(lambda : {})

        def get_grp(s, group):
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

        for acc in accounts:
            get_grp(acc[1] ,groups[acc[0]])
            for i in range(2,len(acc)):
                groups[acc[0]][get_grp(acc[i-1] ,groups[acc[0]])] = get_grp(acc[i] ,groups[acc[0]])

        res = []
        for grp in groups:
            h = defaultdict(lambda : [])
            for x in groups[grp]:
                h[get_grp(x,groups[grp])].append(x)
                
            for x in h:
                res.append([grp]+sorted(h[x]))
        
        return res