# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        W = [set([c for c in x]) for x in words]
        res = 0
        for i in range(len(W)):
            for j in range(i):
                if len(W[i] & W[j]) == 0:
                    res = max(res, len(words[i])*len(words[j]))
        return res