# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self):
        self.next = None
        self.val = 0

class MyLinkedList:

    def __init__(self):
        self.head = Node()

    def get(self, index: int) -> int:
        p = self.head
        for i in range(index+1):
            if p.next == None:
                return -1
            p = p.next

        return p.val

    def addAtHead(self, val: int) -> None:
        n = Node()
        n.val = val
        n.next = self.head.next
        self.head.next = n
        

    def addAtTail(self, val: int) -> None:
        n = Node()
        n.val = val
        p = self.head
        while p.next != None:
            p = p.next
        p.next = n
        

    def addAtIndex(self, index: int, val: int) -> None:
        p = self.head
        for i in range(index):
            if p.next == None:
                return
            p = p.next
        n = Node()
        n.val = val
        n.next = p.next
        p.next = n

    def deleteAtIndex(self, index: int) -> None:
        p = self.head
        for i in range(index):
            if p.next == None:
                return
            p = p.next
        if p.next != None:
            p.next = p.next.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)