# Problem:  Add Binary - https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        bits = 0
        a = [x for x in reversed(a)]
        b = [x for x in reversed(b)]
        if(len(a) < len(b)):
            a,b = b,a
        res = []
        for i in range(len(b)):
            if a[i] == '1':
                bits += 1
            if b[i] == '1':
                bits += 1
            res.append('1' if bits&1 else '0')
            bits >>= 1
        for i in range(len(b), len(a)):
            if a[i] == '1':
                bits += 1
            res.append('1' if bits&1 else '0')
            bits >>= 1
        if bits:
            res.append('1')
        res.reverse()
        return "".join(res)