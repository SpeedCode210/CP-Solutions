# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

from heapq import heappop, heappush
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Hi:
    def __init__(self, node=None):
        self.node = node
    def __lt__(self, nxt):
        if nxt.node is None :
            return False
        return self.node.val < nxt.node.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode()
        x = res
        heap = []
        for l in lists:
            if l is not None:
                heappush(heap, (l.val, Hi(l)))
        
        while len(heap):
            a = heap[0]
            heappop(heap)
            if a[1].node.next is not None:
                heappush(heap, (a[1].node.next.val, Hi(a[1].node.next)))
            x.next = ListNode(a[0])
            x= x.next

        return res.next