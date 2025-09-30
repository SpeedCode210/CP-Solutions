# Problem: Extra Characters in a String - https://leetcode.com/problems/extra-characters-in-a-string/description/

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
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie()
        for x in dictionary:
            trie.insert(x)
        
        dp = [len(s)]*len(s) + [0]

        for i in range(len(s)-1, -1, -1):
            curr = trie.root
            dp[i] = dp[i+1] + 1
            j = i
            while True:
                if j >= len(s) or curr.children[ord(s[j]) - ord('a')] is None:
                    break
                curr = curr.children[ord(s[j]) - ord('a')]
                j += 1
                if curr.is_end:
                    dp[i] = min(dp[i], dp[j])
        
        return dp[0]


