# Problem: Middle of the Linked List - https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p0 = head
        p1 = head
        for i in range(2000):
            p1 = p1.next
            if p1 == None:
                return p0
            if i%2 == 0:
                p0 = p0.next