# Problem: Find All Anagrams in a String - https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        res = []
        D = defaultdict(int)
        for c in p:
            D[c] += 1
        C = 0
        for c in "qwertyuiopasdfghjklzxcvbnm":
            if D[c] == 0:
                C += 1

        for i in range(len(p)):
            if D[s[i]] == 0:
                C -= 1
            D[s[i]] -= 1
            if D[s[i]] == 0:
                C += 1
        if C == 26:
            res = [0]
        for i in range(len(p), len(s)):
            if D[s[i]] == 0:
                C -= 1
            D[s[i]] -= 1
            if D[s[i]] == 0:
                C += 1

            if D[s[i - len(p)]] == 0:
                C -= 1
            D[s[i - len(p)]] += 1
            if D[s[i - len(p)]] == 0:
                C += 1
            if C == 26:
                res.append(i - len(p) + 1)
                print(D)
        return res
