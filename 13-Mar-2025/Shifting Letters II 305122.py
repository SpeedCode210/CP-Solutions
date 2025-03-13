# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        res = []
        x = []
        for i in range(len(s)):
            x.append((i,0,0))
        for shift in shifts:
            x.append((shift[0],-1,shift[2]))
            x.append((shift[1],1,1-shift[2]))
        x.sort()
        delta = 0
        for u in x:
            if u[1] == 0:
                res.append(chr((((delta + ord(s[u[0]]) - ord('a'))%26)+26)%26 + ord('a')))
            else:
                if u[2] == 0:
                    delta -= 1
                else:
                    delta += 1
        return "".join(res)