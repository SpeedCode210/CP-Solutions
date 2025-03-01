# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        I = 0
        count = 0
        for i in range(len(mat)):
            h = sum([x for x in mat[i] if x == 1])
            if h > count:
                count = h
                I = i
        return [I,count]