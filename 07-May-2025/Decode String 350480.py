# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def f(self):
        res = ""
        num = 0
        while True:
            print(self.S)
            if self.S[0].isdigit():
                num = num*10 + ord(self.S[0]) - ord("0")
                self.S = self.S[1:]
            elif self.S[0] == "[":
                self.S = self.S[1:]
                res += self.f()*num
                num = 0
            elif self.S[0] == "]":
                self.S = self.S[1:]
                return res
            else:
                res += self.S[0]
                self.S = self.S[1:]
        
    def decodeString(self, s: str) -> str:
        self.S = s + ']'
        return self.f()