# Problem: First Unique Character in a String - https://leetcode.com/problems/first-unique-character-in-a-string/description/?envType=problem-list-v2&envId=queue

from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        C = Counter(s)
        x = [c for c in C if C[c] == 1]
        if len(x) == 0:
            return -1
        for i in range(len(s)):
            if s[i] in x:
                return i