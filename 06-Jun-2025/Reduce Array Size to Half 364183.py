# Problem: Reduce Array Size to Half - https://leetcode.com/problems/reduce-array-size-to-the-half/

from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        C = Counter(arr)
        a = [C[x] for x in C]
        a.sort(reverse=True)
        S = sum(a)
        somme = 0
        i = 0
        while somme*2 < S:
            somme += a[i]
            i += 1
        return i