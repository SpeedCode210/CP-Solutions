# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node, patapim = 0):
            nonlocal res
            if node is None:
                return
            patapim = patapim*10 + node.val
            if node.left is None and node.right is None:
                res += patapim
                return
            dfs(node.left, patapim)
            dfs(node.right, patapim)
        dfs(root)
        return res