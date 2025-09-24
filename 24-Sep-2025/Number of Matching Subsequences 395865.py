# Problem: Number of Matching Subsequences - https://leetcode.com/problems/number-of-matching-subsequences/

class Node:
    def __init__(self):
        self.children = [None]*26
        self.is_end = 0

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        root = Node()
        for word in words:
            curr = root
            for letter in word:
                idx = ord(letter) - ord('a')
                if curr.children[idx] is None:
                    curr.children[idx] = Node()
                curr = curr.children[idx]
            curr.is_end += 1
        
        count = 0   

        arr = [[len(s)]*26 for _ in range(len(s))]

        arr[-1][ord(s[-1]) - ord('a')] = len(s) - 1

        for i in range(len(s)-2, -1, -1):
            for x in range(26):
                arr[i][x] = arr[i+1][x]
            arr[i][ord(s[i]) - ord('a')] = i

        def test_string(idx : int, t : Node):
            nonlocal count
            nonlocal s
            count += t.is_end
            t.is_end = 0
            if idx >= len(s):
                return

            for i in range(26):
                if t.children[i] is not None and arr[idx][i] < len(s):
                    test_string(arr[idx][i]+1, t.children[i])
                    t.children[i] = None


        test_string(0, root)

        return count
