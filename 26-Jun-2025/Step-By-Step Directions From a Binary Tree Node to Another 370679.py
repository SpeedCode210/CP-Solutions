# Problem: Step-By-Step Directions From a Binary Tree Node to Another - https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        RES = None
        c = 0
        d = 0
        def dfs(node, w = 0):
            nonlocal RES, c, d
            if RES is not None:
                return [False, False]
            if node is None:
                return [False, False]
            res= [False,False]
            if node.val == startValue:
                c = w
                res[0] = True
            if node.val == destValue:
                res[1] = True

            h = dfs(node.left, w+1)
            if RES is not None:
                return [False, False]
            l = dfs(node.right, w+1)
            if RES is not None:
                return [False, False]
            res = [res[0] or h[0] or l[0], res[1] or h[1] or l[1]]

            if res[0] and res[1]:
                d = w
                RES = node  
            node.b = res[1]
            return res

        dfs(root)
        output = ['U']*(c-d)

        while RES.val != destValue:
            if RES.right is None:
                RES = RES.left
                output.append("L")
            elif RES.left is None:
                RES = RES.right
                output.append("R")
            else:
                if RES.right.b:
                    RES = RES.right
                    output.append("R")
                else:
                    RES = RES.left
                    output.append("L")

        return "".join(output)