# Problem: Rotate Image - https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range((n+1)//2):
            for j in range(n//2):
                A = (i,j)
                B = (j, n-1-i)
                C = (n-1-i, n-1-j)
                D = (n-1-j, i)

                matrix[A[0]][A[1]], matrix[B[0]][B[1]] = matrix[B[0]][B[1]], matrix[A[0]][A[1]]
                matrix[A[0]][A[1]], matrix[C[0]][C[1]] = matrix[C[0]][C[1]], matrix[A[0]][A[1]]
                matrix[A[0]][A[1]], matrix[D[0]][D[1]] = matrix[D[0]][D[1]], matrix[A[0]][A[1]]
        