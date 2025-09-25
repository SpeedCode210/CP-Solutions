# Problem:  Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/description/

class Node:
    def __init__(self):
        self.children = [None]*26
        self.is_end = False
        self.val = 0

class Trie:
    def __init__(self):
        self.root = Node()
        self.root.is_end = True
        

    def insert(self, word: str) -> None:
        curr = self.root
        for letter in word:
            idx = ord(letter) - ord('a')
            if curr.children[idx] is None:
                curr.children[idx] = Node()
            curr = curr.children[idx]
        curr.is_end = True
        
class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for x in words:
            trie.insert(x)

        res = 0
        dfs = [(trie.root, "")]
        while len(dfs):
            u = []
            for x, y in dfs:
                if x.is_end:
                    for i, c in enumerate(x.children):
                        if c is not None and c.is_end:
                            u.append((c, y + chr(i + ord('a'))))
            if len(u) == 0:
                return dfs[0][1]
            dfs = u
            res += 1
        