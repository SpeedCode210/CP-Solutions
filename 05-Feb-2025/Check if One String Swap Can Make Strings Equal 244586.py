# Problem: Check if One String Swap Can Make Strings Equal - https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        indicies = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                indicies.append(i)
        if len(indicies) == 0:
            return True
        if len(indicies) != 2:
            return False
        return s1[indicies[0]] == s2[indicies[1]] and s1[indicies[1]] == s2[indicies[0]]
        