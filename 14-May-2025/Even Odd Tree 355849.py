# Problem: Even Odd Tree - https://leetcode.com/problems/even-odd-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        mini = [10000000]*100000
        maxi = [0]*100000
        stack = [root]
        for i in range(100000000):
            if len(stack) == 0:
                break
            if stack[0].val%2 == i%2:
                return False
            for j in range(1,len(stack)):
                if ((-1)**i)*(stack[j].val - stack[j-1].val) <= 0 or stack[j].val%2 == i%2:
                    return False
                    
            stack = [(stack[j//2].left if j%2 == 0 else stack[j//2].right) for j in range(len(stack)*2) if (stack[j//2].left if j%2 == 0 else stack[j//2].right) != None ]

        return True