# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
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
        
        for X in equations:
            if '!' not in X:
                group[get_grp(X[0])] = get_grp(X[3])

        for X in equations:
            if '!' in X:
                if get_grp(X[0]) == get_grp(X[3]):
                    return False
        print(group)
        return True