# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class Node :
    def __init__(self):
        self.children = [None]*26
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for x in word:
            if curr.children[ord(x)-ord('a')] is None:
                curr.children[ord(x)-ord('a')] = Node()
            curr = curr.children[ord(x)-ord('a')]
        curr.is_end = True

    def search(self, word: str, idx = 0, t = None) -> bool:
        if t is None:
            t = self.root
        if idx == len(word):
            return t.is_end
        if word[idx] == '.':
            for i in range(26):
                if t.children[i] is not None and self.search(word, idx+1, t.children[i]):
                    return True
            return False
        
        if t.children[ord(word[idx]) - ord('a')] is None:
            return False
        return self.search(word, idx+1, t.children[ord(word[idx]) - ord('a')])


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)