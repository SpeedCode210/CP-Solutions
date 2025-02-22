# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        return [[1 - image[i][len(image[i]) - j - 1] for j in range(len(image[i]))] for i in range(len(image))]