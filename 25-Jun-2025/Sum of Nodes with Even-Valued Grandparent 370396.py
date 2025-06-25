# Problem: Sum of Nodes with Even-Valued Grandparent - https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        res = 0
        stack = [[1, 1, root]]

        while len(stack):
            p = stack[-1]
            stack.pop()
            if p[2] is None:
                continue
            if p[0]%2 == 0:
                res += p[2].val
            stack.append([p[1], p[2].val, p[2].left])
            stack.append([p[1], p[2].val, p[2].right])
        return res