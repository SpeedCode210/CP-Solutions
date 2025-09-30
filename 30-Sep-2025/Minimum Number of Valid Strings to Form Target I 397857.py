# Problem: Minimum Number of Valid Strings to Form Target I - https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-i/description/

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
    def minValidStrings(self, words: List[str], target: str) -> int:
        trie = Trie()
        for x in words:
            trie.insert(x)
        
        dp = [len(target)+1]*len(target) + [0]

        for i in range(len(target)-1, -1, -1):
            curr = trie.root
            j = i
            while True:
                if j >= len(target) or curr.children[ord(target[j]) - ord('a')] is None:
                    break
                curr = curr.children[ord(target[j]) - ord('a')]
                j += 1
                dp[i] = min(dp[i], dp[j]+1)
        
        return dp[0] if dp[0] <= len(target) else -1
