# Problem: K-th Symbol in Grammar - https://leetcode.com/problems/k-th-symbol-in-grammar/description/

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        k -= 1
        res = 0
        while k > 0:
            res = (res+k%2)%2
            k = k//2
        return res