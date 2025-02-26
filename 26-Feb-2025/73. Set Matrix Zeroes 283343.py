# Problem: 73. Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/description/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        x,y = -1,-1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    x,y = i,j
        
        if x == -1:
            return


        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[x][j] = 0
                    matrix[i][y] = 0
        
        for i in range(len(matrix)):
            if x == i: 
                continue
            if matrix[i][y] == 0:
                for j in range(len(matrix[0])):
                    matrix[i][j] = 0

        for j in range(len(matrix[0])):
            if y == j: 
                continue
            if matrix[x][j] == 0:
                for i in range(len(matrix)):
                    matrix[i][j] = 0

        for i in range(len(matrix)):
            matrix[i][y] = 0
        
        for j in range(len(matrix[0])):
            matrix[x][j] = 0

