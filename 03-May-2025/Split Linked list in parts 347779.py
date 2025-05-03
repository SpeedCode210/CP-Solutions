# Problem: Split Linked list in parts - https://leetcode.com/problems/split-linked-list-in-parts/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        if head == None:
            return [None]*k
        
        n = 0
        h = head
        while h!= None:
            n += 1
            h = h.next
        h = head
        res = [head]
        baseLen = n // k

        if baseLen == 0:
            J = head
            while J.next != None:
                res.append(J.next)
                J.next = None
                J = res[-1]

            while(len(res) < k):
                res.append(None)
            return res

        for i in range(k-1):
            for j in range(baseLen-1 + (1 if i < n%(k) else 0)):
                h = h.next
            res.append(h.next)
            u = h
            h = h.next
            u.next = None
        while(len(res) < k):
            res.append(None)
        return res