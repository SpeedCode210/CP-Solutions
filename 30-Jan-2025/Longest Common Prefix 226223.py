# Problem: Longest Common Prefix - https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ""
        le = 100000000000
        for e in strs:
            le = min(le,len(e))
        for i in range(0,le):
            for j in range(1,len(strs)):
                if strs[j][i] != strs[j-1][i]:
                    return s
            s = s + strs[0][i]
        return s