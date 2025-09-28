# Problem: Partition String  - https://leetcode.com/problems/partition-string/description/

class Node:
    def __init__(self):
        self.children = {}

class Solution:
    def partitionString(self, s: str) -> List[str]:
        root = Node()
        res = []
        curr_word = []
        curr = root
        for x in s:
            curr_word.append(x)
            if x in curr.children:
                curr = curr.children[x]
            else:
                curr.children[x] = Node()
                res.append("".join(curr_word))
                curr_word = []
                curr = root
        return res