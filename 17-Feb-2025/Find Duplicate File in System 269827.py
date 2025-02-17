# Problem: Find Duplicate File in System - https://leetcode.com/problems/find-duplicate-file-in-system/

from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        D = defaultdict(lambda : [])
        for path in paths:
            x = path.split()
            for i in range(1, len(x)):
                c = x[i].split("(")
                D[c[1]].append(x[0]+"/"+c[0])
        
        return [D[s] for s in D if len(D[s]) > 1]