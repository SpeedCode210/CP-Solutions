# Problem: Short Encoding of Words - https://leetcode.com/problems/short-encoding-of-words/

class Node:
    def __init__(self):
        self.children = [None]*26
        self.is_end = True
        self.depth = 0

class Trie:
    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for letter in word:
            idx = ord(letter) - ord('a')
            if curr.children[idx] is None:
                curr.children[idx] = Node()
                curr.children[idx].depth = curr.depth+1
            curr = curr.children[idx]
        curr.is_end = True

    def export(self) -> int:
        cnt = 0

        dfs = [self.root]
        while len(dfs):
            a = dfs[-1]
            dfs.pop()
            add = True
            for x in a.children:
                if x is not None:
                    add = False
                    dfs.append(x)
            if add:
                cnt += a.depth+1
        return cnt


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = Trie()
        for i, x in enumerate(words):
            trie.insert(reversed(x))

        return trie.export()
        