# Problem: Partition List - https://leetcode.com/problems/partition-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        h1 = ListNode()
        t1 = h1
        h2 = ListNode()
        t2 = h2
        u = head
        while u != None:
            i = u
            u = u.next
            if i.val < x:
                t1.next = i
                t1 = i
            else:
                t2.next = i
                t2 = i
            i.next = None
        
        t1.next = h2.next
        return h1.next