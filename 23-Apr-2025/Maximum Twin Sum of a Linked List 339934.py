# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = head
        res = None
        while h != None :
            u = h.next
            h.next = res
            res = h
            h = u

        return res

    def pairSum(self, head: Optional[ListNode]) -> int:
        p1 = head
        p2 = head
        i = 0

        while p1.next != None:
            p1 = p1.next
            if i%2 == 0 and i > 0:
                p2 = p2.next
            i += 1


        p2.next = self.reverseList(p2.next)
        p1 = head
        p2 = p2.next
        res = 0
        while p2 is not None :
            res = max(res, p1.val + p2.val)
            p1 = p1.next
            p2 = p2.next
        return res