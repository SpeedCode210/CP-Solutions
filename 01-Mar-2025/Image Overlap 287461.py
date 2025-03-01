# Problem: Image Overlap - https://leetcode.com/problems/image-overlap/description/

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        def hi(x,y):
            if x < 0 or y < 0 or x >= len(img1) or y >= len(img1):
                return 0
            return img1[x][y]
            
        res = [0]*(4*len(img1)**2)

        for i in range(len(img1)):
            for j in range(len(img1)):
                if img2[i][j] == 0:
                    continue
                s = 0
                for X in range(-len(img1), len(img1)):
                    for Y in range(-len(img1), len(img1)):
                        res[s] += img2[i][j] * hi(i+X,j+Y)
                        s += 1

        return max(res)