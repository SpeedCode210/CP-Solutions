# Problem: Copy List with Random Pointer - https://leetcode.com/problems/copy-list-with-random-pointer/

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        
        N = Node(head.val)
        
        n = N
        h = head
        while h.next != None:
            n.next = Node(h.next.val)
            n = n.next
            h = h.next

        n = N
        h = head
        while h != None:
            if h.random == None:
                n = n.next
                h = h.next
                continue
            
            x = N
            y = head

            while y != h.random:
                x = x.next
                y = y.next
            n.random = x

            n = n.next
            h = h.next

        return N