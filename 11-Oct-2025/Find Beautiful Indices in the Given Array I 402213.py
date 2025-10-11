# Problem: Find Beautiful Indices in the Given Array I - https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-i/description/

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        if len(b) > len(s) or len(a) > len(s):
            return []
            
        def kmp(x : str) -> List[int]:
            arr = [0]*len(x)
            i = 0
            j = 1
            while j < len(x):
                if x[i] == x[j]:
                    arr[j] = i+1
                    i += 1
                    j += 1
                elif i != 0:
                    i = arr[i-1]
                else:
                    j += 1
            return arr

        def match(X : str, x : str, km : List[int]) -> List[int]:
            p = 0
            arr = [0]*len(X)
            j = 0
            while j < len(X):
                if x[p] == X[j]:
                    arr[j] = p+1
                    p += 1
                    j += 1
                elif p != 0:
                    p = km[p-1]
                else:
                    j += 1
            return arr
        
        K1 = kmp(a + "?")
        K2 = kmp(b + "?")

        m1 = match(s, a+"?", K1)
        m2 = match(s, b+"?", K2)
        
        m2 = [0] + [1 if m2[i] == len(b) else 0 for i in range(len(s))]
        for i in range(len(s)):
            m2[i+1] += m2[i]

        res = []

        for i in range(len(s) - len(a) + 1):
            if m1[i+len(a)-1] == len(a) and m2[min(len(s), i+len(b) + k)] - m2[max(0, min(i+len(b)-1 - k, len(s)))] > 0:
                res.append(i)

        return res

        