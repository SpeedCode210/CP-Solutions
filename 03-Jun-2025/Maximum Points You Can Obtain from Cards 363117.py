# Problem: Maximum Points You Can Obtain from Cards - https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        S = sum(cardPoints)
        if k == len(cardPoints):
            return S
        n = len(cardPoints) - k
        u = sum(cardPoints[:n])
        res = S - u
        for i in range(n, len(cardPoints)):
            u -= cardPoints[i-n]
            u += cardPoints[i]
            res = max(res, S-u)
        return res