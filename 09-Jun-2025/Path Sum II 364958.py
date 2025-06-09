# Problem: Path Sum II - https://leetcode.com/problems/path-sum-ii/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        cache = []
        res = []
        somme = [0]
        def f(node):
            if node is None:
                if somme[0] == targetSum and len(cache) > 0:
                    res.append([x for x in cache])
                return
            
            cache.append(node.val)
            somme[0] += node.val
            if node.left is None and node.right is None:
                f(None)
            else:
                if node.left is not None:
                    f(node.left)
                if node.right is not None:
                    f(node.right)
            somme[0] -= node.val
            cache.pop()

        f(root)
        return res