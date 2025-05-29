# Problem: Validate Binary Search Tree - https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(node):
            mini = node.val
            maxi = node.val
            if node.right != None:
                a = check(node.right)
                if (not a[0]) or a[1] <= node.val:
                    return (False,0,0)
                mini = min(mini,a[1])
                maxi = max(maxi,a[2])
                
            if node.left != None:
                a = check(node.left)
                if (not a[0]) or a[2] >= node.val:
                    return (False,0,0)
                mini = min(mini,a[1])
                maxi = max(maxi,a[2])
            return (True, mini, maxi)
        
        return check(root)[0]