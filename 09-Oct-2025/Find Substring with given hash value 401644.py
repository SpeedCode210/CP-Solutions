# Problem: Find Substring with given hash value - https://leetcode.com/problems/find-substring-with-given-hash-value/description/

class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        res = 100000000
        H = pow(power, k-1, modulo)

        h = 0
        for i in range(len(s)-1, len(s)-k-1, -1):
            h *= power
            h += ord(s[i])-ord('a') + 1
            h %= modulo

        if h == hashValue:
            res = len(s)-k
        
        for i in range(len(s)-k-1, -1, -1):
            h -= H*(ord(s[i+k])-ord('a') + 1)
            h *= power
            h += ord(s[i])-ord('a') + 1
            h = (h%modulo + modulo)%modulo

            if h == hashValue:
                res = i

        return s[res:res+k]
        

