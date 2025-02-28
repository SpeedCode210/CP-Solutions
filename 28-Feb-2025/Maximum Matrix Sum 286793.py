# Problem: Maximum Matrix Sum - https://leetcode.com/problems/maximum-matrix-sum/description/?envType=problem-list-v2&envId=matrix

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        mini = 1000000000
        nb = 0
        somme = 0
        for i in range(n):
            for j in range(n):
                if matrix[i][j] < 0:
                    nb += 1
                mini = min(abs(matrix[i][j]), mini)
                somme += abs(matrix[i][j])
        if nb%2 == 0:
            return somme
        return somme - 2*mini
        