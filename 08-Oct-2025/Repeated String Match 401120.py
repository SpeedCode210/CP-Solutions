# Problem: Repeated String Match - https://leetcode.com/problems/repeated-string-match/description/

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        r = a*(len(b)//len(a)+2)
        u = b + r
        kmp = [0]*len(u)

        i,j = 0,1

        while j < len(u):
            if u[j] == u[i] :
                kmp[j] = i+1
                j += 1
                i += 1
            elif i == 0:
                j += 1
            else:
                i = kmp[i-1]

            if kmp[j-1] >= len(b) and j >= 2*len(b):
                return (j-1-len(b))//len(a) + 1

        return -1