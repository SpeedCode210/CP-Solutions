# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

S = ""
class Solution:
    def f(self):
        print(self.S)
        self.S = self.S[1:]
        res = 0
        while self.S[0] == "(":
            res += self.f()
        self.S = self.S[1:]
        return 2*res if res > 0 else 1

    def scoreOfParentheses(self, s: str) -> int:
        self.S = s
        
        RES = 0
        while len(self.S) > 0:
            RES += self.f()
        return RES
                
            