# Problem: Path Sum - https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int, flag = False) -> bool:
        if root == None :
            return targetSum == 0 and flag
        if root.left is None:
            return self.hasPathSum(root.right, targetSum-root.val, True)
        if root.right is None:
            return self.hasPathSum(root.left, targetSum-root.val, True)
        return self.hasPathSum(root.left, targetSum-root.val, True) or self.hasPathSum(root.right, targetSum-root.val, True)