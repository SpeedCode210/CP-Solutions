# Problem: Pascal's Triangle - https://leetcode.com/problems/pascals-triangle/description/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        x = self.generate(numRows-1)
        return x + [ [(0 if i == 0 else x[-1][i-1])+(0 if i == numRows-1 else x[-1][i]) for i in range(numRows)] ]