# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return [""]
        res = []
        for i in range(n):
            x = self.generateParenthesis(i)
            y = self.generateParenthesis(n-1-i)
            for u in x:
                for v in y:
                    res.append('(' + u + ')' + v)
        return res