# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
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

        for i in range(len(s1)):
            group[max(get_grp(s1[i]),get_grp(s2[i]))] = min(get_grp(s1[i]),get_grp(s2[i]))

        return "".join([get_grp(x) for x in baseStr])
