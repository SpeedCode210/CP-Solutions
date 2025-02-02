# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskEmail(self, s) -> str:
        for i in range(1,len(s)):
            if s[i] == '@':
                return s[0] + "*****" + s[i-1:]

    def maskNumber(self, s) -> str:
        k = []
        for c in s:
            if c >= "0" and c <= "9":
                k.append(c)
        s = '***-***-' + "".join(k[-4:])
        if len(k) == 10:
            return s
        return "+" + ("*"*(len(k)-10)) + "-" + s

    def maskPII(self, s: str) -> str:
        s = s.lower()
        mail = False
        for c in s:
            if c == "@":
                mail = True
        if mail:
            return self.maskEmail(s)
        return self.maskNumber(s)
    