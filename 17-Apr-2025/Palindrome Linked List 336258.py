# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

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
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        n = 1
        p = head
        while p.next != None:
            p = p.next
            n += 1

        p = head
        for i in range((n+1)//2):
            p = p.next
        P = self.reverseList(p)
        Q = head

        for i in range(n//2):
            if P.val != Q.val:
                return False
            P = P.next
            Q = Q.next
        return True
        