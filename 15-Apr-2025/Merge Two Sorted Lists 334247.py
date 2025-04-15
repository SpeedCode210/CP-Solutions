# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        lst = ListNode(min(list1.val, list2.val))
        pt = lst
        if lst.val == list1.val:
            list1 = list1.next
        else:
            list2 = list2.next
        while list1 != None or list2 != None:
            if list1 == None:
                pt.next = list2
                break
            if list2 == None:
                pt.next = list1
                break
            pt.next = ListNode(min(list1.val, list2.val))
            pt = pt.next
            if pt.val == list1.val:
                list1 = list1.next
            else:
                list2 = list2.next
        return lst

        