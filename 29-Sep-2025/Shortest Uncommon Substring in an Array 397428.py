# Problem: Shortest Uncommon Substring in an Array - https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/description/

class Node:
    def __init__(self):
        self.children = [None]*26
        self.is_end = 0

class Trie:
    def __init__(self):
        self.root = Node()
        

    def add(self, word: str) -> None:
        curr = self.root
        for letter in word:
            idx = ord(letter) - ord('a')
            if curr.children[idx] is None:
                curr.children[idx] = Node()
            curr = curr.children[idx]
            curr.is_end += 1

    def remove(self, word: str) -> None:
        curr = self.root
        for letter in word:
            idx = ord(letter) - ord('a')
            if curr.children[idx] is None:
                curr.children[idx] = Node()
            curr = curr.children[idx]
            curr.is_end -= 1

    def find(self, word: str) -> str:
        curr = self.root
        for i, letter in enumerate(word):
            idx = ord(letter) - ord('a')
            if curr.children[idx] is None:
                curr.children[idx] = Node()
            curr = curr.children[idx]
            if curr.is_end == 0:
                return word[:i+1]
        
        return ""

    

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        trie = Trie()
        for x in arr:
            for i in range(len(x)):
                trie.add(x[i:])

        res = []
        for x in arr:
            resu = ""
            for i in range(len(x)):
                trie.remove(x[i:])
            
            for i in range(0, len(x)):
                s = trie.find(x[i:])
                if s != "":
                    if resu == "" or len(s) < len(resu) or (len(s) == len(resu) and s < resu):
                        resu = s

            res.append(resu)
            for i in range(len(x)):
                trie.add(x[i:])
        
        return res