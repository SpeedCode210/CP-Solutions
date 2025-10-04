# Problem: Remove Sub-Folders from the Filesystem - https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = Node()

        for x in folder:
            y = x[1:].split('/')
            curr = root
            for z in y:
                if z not in curr.children:
                    curr.children[z] = Node()
                curr = curr.children[z]
            curr.is_end = True
        
        res = []
        def explore(node, curr = ""):
            nonlocal res
            if node.is_end:
                res.append(curr)
                return
            for x in node.children:
                explore(node.children[x], curr + "/" + x)

        explore(root)
        return res