# Problem: Rotate List - https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return None
        tail = head
        n = 1
        while tail.next != None:
            tail = tail.next
            n += 1

        k %= n

        tail.next = head

        q = head
        for i in range(n - k - 1):
            q = q.next
        beg = q.next
        q.next = None

        return beg