# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        S1 = [0]*26
        S2 = [0]*26
        for c in s1:
            S1[ord(c) - ord('a')] += 1

        for i,c in enumerate(s2):
            if i < len(s1):
                S2[ord(c) - ord('a')] += 1
                count = 0
                for i in range(26):
                    if S1[i] == S2[i]:
                        count += 1
                if count == 26:
                    return True
            else:
                S2[ord(c) - ord('a')] += 1
                S2[ord(s2[i-len(s1)]) - ord('a')] -= 1
                count = 0
                for i in range(26):
                    if S1[i] == S2[i]:
                        count += 1
                if count == 26:
                    return True
        return False
