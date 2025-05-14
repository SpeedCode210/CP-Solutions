# Problem: Maximum Binary Tree - https://leetcode.com/problems/maximum-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        i = 0
        for j in range(1, len(nums)):
            if nums[j] > nums[i]:
                i = j
        
        n = TreeNode(nums[i])
        n.left = self.constructMaximumBinaryTree(nums[:i])
        n.right = self.constructMaximumBinaryTree(nums[i+1:])
        return n