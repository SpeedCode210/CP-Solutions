# Problem: Delete Duplicate Folders in System - https://leetcode.com/problems/delete-duplicate-folders-in-system/description/

from collections import defaultdict
P = 99194853094755497
Q = 99194853094753497
R1 = 7623147
R1b = 6432311
R2 = 27
R3 = 93

class Node:
    def __init__(self, text : str):
        self.children = {}
        self.hash = [None, None]
        self.text = text

    def get_text_hash(self):
        h = 0
        for x in self.text:
            h *= R2
            h += ord(x) - ord('a') + 1
            h %= Q
        return h

    def get_hash(self, i):
        if self.hash[i] is None:
            h = 0
            X = [(self.children[x].get_hash(j%2)*R3 + self.children[x].get_text_hash())%P for j,x in enumerate(self.children)]
            X.sort()
            for x in X:
                h *= R1 if i == 0 else R1b
                h += x
                h %= P
            self.hash[i] = h

        return self.hash[i]

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        trie = Node("ROOT")
        for X in paths:
            curr = trie
            for y in X:
                if y not in curr.children:
                    curr.children[y] = Node(y)
                curr = curr.children[y]
        D = defaultdict(int)
        D[trie.get_hash(0)] -= 1

        def explore(node):
            D[node.get_hash(0)] += 1
            for x in node.children:
                explore(node.children[x])
                
        explore(trie)

        res = []
        curr = []
        

        def process(node):
            if D[node.get_hash(0)] > 1 and len(node.children) > 0:
                curr.append(node.text)
                print(curr, node.get_hash(0))
                curr.pop()
                return
            curr.append(node.text)
            res.append([x for x in curr])
            for x in node.children:
                process(node.children[x])
            curr.pop()

        for x in trie.children:
            process(trie.children[x])

        return res