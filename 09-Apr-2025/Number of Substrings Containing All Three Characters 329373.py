# Problem: Number of Substrings Containing All Three Characters - https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res = 0
        arr = [-1,-1,-1]
        for i in range(len(s)):
            if s[i] == 'a':
                arr[0] = i
            elif s[i] == 'b':
                arr[1] = i
            elif s[i] == 'c':
                arr[2] = i
            if min(arr) > -1:
                res += min(arr) + 1

        return res