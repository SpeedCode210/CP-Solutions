# Problem: Minimum Number of Operations to Move All Balls to Each Box - https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        right = 0 
        nb_right = 0
        for i in range(len(boxes)):
            if boxes[i] == '1':
                right += i
                nb_right += 1
        nb_left = 0
        left = 0
        res = []
        for i in range(len(boxes)):
            res.append( right - nb_right*i + nb_left*i - left )
            if boxes[i] == '1':
                nb_left += 1
                nb_right -= 1
                left += i
                right -= i

        
        return res