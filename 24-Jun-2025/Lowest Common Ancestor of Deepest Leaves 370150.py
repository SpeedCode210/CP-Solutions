# Problem: Lowest Common Ancestor of Deepest Leaves - https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import sys, threading

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root.depth = 0
        stack = [root]
        while len(stack):
            s = stack[-1]
            stack.pop()
            if s.left is not None:
                s.left.depth = s.depth + 1
                stack.append(s.left)
            if s.right is not None:
                s.right.depth = s.depth + 1
                stack.append(s.right)
        
        def f(node):
            node.h = node.depth
            if node.left is not None:
                node.h = max(node.h, f(node.left))
            if node.right is not None:
                node.h = max(node.h, f(node.right))
            return node.h
        
        f(root)
        curr = root
        while True:
            if curr.left is None and curr.right is None:
                return curr
            if curr.left is None:
                curr = curr.right
            elif curr.right is None:
                curr = curr.left
            elif curr.left.h == curr.right.h:
                return curr
            elif curr.left.h > curr.right.h:
                curr = curr.left
            else:
                curr = curr.right
        
