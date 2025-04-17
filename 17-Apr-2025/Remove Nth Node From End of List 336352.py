# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        m = 0
        h = head
        while h != None:
            h = h.next
            m += 1
        index = m - n
        if index == 0:
            return head.next

        h = head
        for i in range(index - 1):
            h = h.next
        h.next = h.next.next
        return head
        