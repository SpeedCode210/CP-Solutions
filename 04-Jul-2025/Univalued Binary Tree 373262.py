# Problem: Univalued Binary Tree - https://leetcode.com/problems/univalued-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if root.left is not None and (root.left.val != root.val or not self.isUnivalTree(root.left)):
            return False
        if root.right is not None and (root.right.val != root.val or not self.isUnivalTree(root.right)):
            return False
        return True