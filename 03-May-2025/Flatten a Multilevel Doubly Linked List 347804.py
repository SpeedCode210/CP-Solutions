# Problem: Flatten a Multilevel Doubly Linked List - https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/description/?envType=problem-list-v2&envId=linked-list

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def f(h: 'Optional[Node]') -> 'Optional[Node]':
            H = h
            last = H
            while H != None :
                last = H
                A = H.next
                if H.child != None:
                    C = f(H.child)
                    H.next = H.child
                    H.child.prev = H
                    C.next = A
                    if A != None:
                        A.prev = C
                        H.child = None
                    else:
                        H.child = None
                        return C
                H = A
            return last

        f(head)

        return head