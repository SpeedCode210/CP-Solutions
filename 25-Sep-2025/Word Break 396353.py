# Problem: Word Break - https://leetcode.com/problems/word-break/description/

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
        dp = [False]*len(s) + [True]
        for i in range(len(s)-1, -1, -1):
            curr = trie.root
            for j in range(i, min(len(s), i+20)):
                curr = curr.children[ord(s[j]) - ord('a')]
                if curr is None:
                    break
                if curr.is_end and dp[j+1]:
                    dp[i] = True
                    break 
        
        return dp[0]