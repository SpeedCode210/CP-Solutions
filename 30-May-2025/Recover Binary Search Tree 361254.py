# Problem: Recover Binary Search Tree - https://leetcode.com/problems/recover-binary-search-tree/description/

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

    def maxi(self,node):
        if node is None:
            return None
        res = node
        a = self.maxi(node.left)
        if a is not None and a.val > res.val:
            res = a
        a = self.maxi(node.right)
        if a is not None and a.val > res.val:
            res = a
        return res
    
    def mini(self,node):
        if node is None:
            return None
        res = node
        a = self.mini(node.left)
        if a is not None and a.val < res.val:
            res = a
        a = self.mini(node.right)
        if a is not None and a.val < res.val:
            res = a
        return res

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return

        if self.isValidBST(root):
            return
        
        a = self.maxi(root.left)
        b = self.mini(root.right)

        if a is not None and b is not None:
            a.val, b.val = b.val, a.val
            if self.isValidBST(root):
                return
            a.val, b.val = b.val, a.val

        if a is not None:
            root.val, a.val = a.val, root.val
            if self.isValidBST(root):
                return
            root.val, a.val = a.val, root.val

        if b is not None:
            root.val, b.val = b.val, root.val
            if self.isValidBST(root):
                return
            root.val, b.val = b.val, root.val
        
        self.recoverTree(root.left)
        self.recoverTree(root.right)
            
        
            