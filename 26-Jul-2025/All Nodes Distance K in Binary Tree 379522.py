# Problem: All Nodes Distance K in Binary Tree - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        bfs = deque([root])
        root.parent = root
        res = []
        while len(bfs):
            x = bfs[0]
            bfs.popleft()
            x.d = -1
            if x.left is not None:
                bfs.append(x.left)
                x.left.parent = x
            if x.right is not None:
                bfs.append(x.right)
                x.right.parent = x

        target.d = 0
        bfs = deque([target])

        while len(bfs):
            x = bfs[0]
            bfs.popleft()
            if x.d == k:
                res.append(x.val)
            if x.left is not None and x.left.d == -1:
                bfs.append(x.left)
                x.left.d = x.d+1
            if x.right is not None and x.right.d == -1:
                bfs.append(x.right)
                x.right.d = x.d+1
            if x.parent is not None and x.parent.d == -1:
                bfs.append(x.parent)
                x.parent.d = x.d+1
        return res