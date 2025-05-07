# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def f(i):
            return matrix[i//len(matrix[0])][i%len(matrix[0])]

        a = 0
        b = len(matrix)*(len(matrix[0])) - 1

        while a <= b:
            m = (a+b+1)//2
            l = f(m)
            if l == target:
                return True
            if l > target:
                b = m-1
            else:
                a = m+1
        return False