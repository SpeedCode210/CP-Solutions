# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [[0,0] for i in range(len(questions))]
        questions.reverse()
        dp[0][0] = questions[0][0]
        for i in range(1, len(questions)):
            dp[i][1] = max(dp[i-1])
            dp[i][0] = questions[i][0] + max([0] if i - questions[i][1]-1 < 0 else dp[i-questions[i][1]-1])
        return max(dp[-1])