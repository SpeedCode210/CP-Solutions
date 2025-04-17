# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
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

        return lst.next