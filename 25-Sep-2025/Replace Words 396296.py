# Problem: Replace Words - https://leetcode.com/problems/replace-words/

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

    def match(self, word : str) -> str:
        curr = self.root
        for i, letter in enumerate(word):
            idx = ord(letter) - ord('a')
            if curr.children[idx] is None:
                return word
            curr = curr.children[idx]
            if curr.is_end:
                return word[:i+1]

        return word


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        
        return " ".join([trie.match(x) for x in sentence.split()])
