# Problem: Edit Distance - https://leetcode.com/problems/edit-distance/description/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        f = [[0 for i in range(len(word1)+1)] for j in range(len(word2)+1)]
        for j in range(len(word1)+1):
            f[0][j] = j
        for i in range(1, len(word2)+1):
            f[i][0] = i
        
        for i in range(1, len(word2)+1):
            for j in range(1, len(word1)+1):
                f[i][j] = f[i-1][j] + 1
                f[i][j] = min(f[i][j], f[i-1][j-1] + 1)
                f[i][j] = min(f[i][j], f[i][j-1] + 1)
                if word2[i-1] == word1[j-1]:
                    f[i][j] = min(f[i][j], f[i-1][j-1])           

        return f[-1][-1]