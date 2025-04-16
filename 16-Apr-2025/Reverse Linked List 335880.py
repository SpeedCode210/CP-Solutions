# Problem: Reverse Linked List - https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        x = self.reverseList(head.next)
        head.next = None
        u = x
        if u == None:
            return head
        while u.next != None:
            u = u.next
        
        u.next = head
        return x