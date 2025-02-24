# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res = []
        i = 0
        j = 0
        
        for i in range(0,len(mat)+len(mat[0])-1):
            if i%2 == 0:
                x = i if i < len(mat) else len(mat)-1
                y = 0 if i < len(mat) else i - len(mat) + 1

                while(x >= 0 and y >= 0 and x < len(mat) and y < len(mat[0])):
                    res.append(mat[x][y])
                    x -= 1
                    y += 1
            else:
                x = 0 if i < len(mat[0]) else i - len(mat[0]) + 1
                y = i if i < len(mat[0]) else len(mat[0]) - 1

                while(x >= 0 and y >= 0 and x < len(mat) and y < len(mat[0])):
                    res.append(mat[x][y])
                    x += 1
                    y -= 1

        return res