# Problem: Greatest Common Divisor of Strings - https://leetcode.com/problems/greatest-common-divisor-of-strings/

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1==str2:
            return str1
        if(len(str1) < len(str2)):
            for i in range(0, len(str1)):
                if str1[i] != str2[i]:
                    return ""
            return self.gcdOfStrings(str1, str2[len(str1):])
        if(len(str1) > len(str2)):
            for i in range(0, len(str2)):
                if str1[i] != str2[i]:
                    return ""
            return self.gcdOfStrings(str1[len(str2):], str2)
        return ""