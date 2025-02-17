# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        C = Counter([c for c in s])
        return "".join(c[1]*C[c[1]] for c in sorted([(-C[i],i) for i in C]))