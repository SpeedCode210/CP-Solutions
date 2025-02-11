# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        D = defaultdict(lambda : [])
        for s in strs:
            key = "".join(sorted([c for c in s]))
            D[key].append(s)
        return [D[x] for x in D]