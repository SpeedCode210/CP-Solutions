# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        res = [[0]*len(img[0]) for i in range(len(img))]
        for i in range(0,len(img)):
            for j in range(0, len(img[0])):
                cells = [(i,j),(i,j+1),(i,j-1),(i+1,j),(i-1,j),(i+1,j+1),(i+1,j-1),(i-1,j+1),(i-1,j-1)]
                res[i][j] = floor(sum([img[x[0]][x[1]] for x in cells if x[0] >=0 and x[0] < len(img) and x[1] < len(img[0]) and x[1] >= 0])/sum([1               for x in cells if x[0] >=0 and x[0] < len(img) and x[1] < len(img[0]) and x[1] >= 0]))
        return res
        