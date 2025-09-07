# Problem: Relative Ranks - https://leetcode.com/problems/relative-ranks/description/

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score = [[y,x] for x,y in enumerate(score)]
        score.sort(key=lambda x : -x[0])
        score[0][0] = 'Gold Medal'
        if len(score) > 1:
            score[1][0] = 'Silver Medal'
        if len(score) > 2:
            score[2][0] = 'Bronze Medal'
        for i in range(3, len(score)):
            score[i][0] = str(i+1)
        score.sort(key=lambda x : x[1])
        return [x[0] for x in score]