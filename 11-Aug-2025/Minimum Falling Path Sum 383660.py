# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        a = matrix[0]
        for i in range(1, len(matrix)):
            if len(a) == 1:
                a = [a[0] + matrix[i][0]]
            else:
                a = [matrix[i][0] + min(a[0:2])] + [matrix[i][j] + min(a[j-1:j+2]) for j in range(1, len(a)-1)] + [matrix[i][-1] + min(a[len(a)-2:len(a)])]
        
        return min(a)