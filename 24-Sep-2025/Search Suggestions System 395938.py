# Problem: Search Suggestions System - https://leetcode.com/problems/search-suggestions-system/

class Node :
    def __init__(self):
        self.children = [None]*26
        self.is_end = False

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        self.root = Node()
        for word in products:
            curr = self.root
            for x in word:
                if curr.children[ord(x)-ord('a')] is None:
                    curr.children[ord(x)-ord('a')] = Node()
                curr = curr.children[ord(x)-ord('a')]
            curr.is_end = True

        res = [[] for i in range(len(searchWord))]

        current = []
        def explore(t, depth = 0, matches = 0):
            nonlocal searchWord
            nonlocal res
            
            if t.is_end:
                for x in range(matches-1, -1, -1):
                    if (len(res[x])) < 3:
                        res[x].append("".join(current))
                    else:
                        break

            for i in range(26):
                if t.children[i] is None:
                    continue
                current.append(chr(ord('a') + i))
                if depth != matches:
                    new_matches = matches
                elif depth < len(searchWord) and chr(ord('a') + i) == searchWord[depth]:
                    new_matches = matches + 1
                else: 
                    new_matches = matches
                explore(t.children[i], depth+1, new_matches)
                current.pop()


        explore(self.root)

        return res
