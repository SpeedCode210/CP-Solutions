# Problem: Add Two Numbers II - https://leetcode.com/problems/add-two-numbers-ii/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, l):
        top = None
        while l != None:
            u = l.next
            l.next = top
            top = l
            l = u
        return top
        
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        lst = ListNode()
        current = lst
        carry = 0
        while carry != 0 or l1 != None or l2 != None:
            if l1 != None:
                carry += l1.val
                l1 = l1.next
            if l2 != None:
                carry += l2.val
                l2 = l2.next
            current.next  = ListNode()
            current = current.next
            current.val = carry % 10
            carry = carry // 10

        return self.reverse(lst.next)