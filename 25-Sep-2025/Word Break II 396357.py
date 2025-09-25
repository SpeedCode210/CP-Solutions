# Problem: Word Break II - https://leetcode.com/problems/word-break-ii/description/

class Node:
    def __init__(self):
        self.children = [None]*26
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for letter in word:
            idx = ord(letter) - ord('a')
            if curr.children[idx] is None:
                curr.children[idx] = Node()
            curr = curr.children[idx]
        curr.is_end = True


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for x in wordDict:
            trie.insert(x)

        dp = [[] for _ in range(len(s))] + [[len(s)]]

        for i in range(len(s)-1, -1, -1):
            curr = trie.root
            for j in range(i, len(s)):
                curr = curr.children[ord(s[j]) - ord('a')]
                if curr is None:
                    break
                if curr.is_end and len(dp[j+1]):
                    dp[i].append(j+1)

        res = []
        curr = []

        def explore(n):
            nonlocal res,curr,dp,s
            if n == len(s):
                res.append(" ".join(curr))
                return
            for x in dp[n]:
                curr.append(s[n:x])
                explore(x)
                curr.pop()
                     
        explore(0)
        
        return res