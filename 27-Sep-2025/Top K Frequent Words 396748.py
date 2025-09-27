# Problem: Top K Frequent Words - https://leetcode.com/problems/top-k-frequent-words/

class Node:
    def __init__(self):
        self.children = [None]*26
        self.is_end = 0

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
        curr.is_end += 1

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        trie = Trie()
        for x in words:
            trie.insert(x)

        res = [[] for _ in range(len(words)+1)]

        curr = []

        def explore(node):
            if node.is_end:
                res[node.is_end].append("".join(curr))
            for i in range(26):
                curr.append(chr(ord('a')+i))
                if node.children[i] is not None:
                    explore(node.children[i])
                curr.pop()
                
        explore(trie.root)
        
        resu = []

        for i in range(len(words), 0, -1):
            for x in res[i]:
                if len(resu) == k:
                    break
                resu.append(x)

        return resu