# Problem: Design Circular Deque - https://leetcode.com/problems/design-circular-deque/

class Node:
    def __init__(self, v = 0):
        self.val = v
        self.next = None
        self.previous = None


class MyCircularDeque:

    def __init__(self, k: int):
        self.front = None
        self.back = None
        self.k = k
        self.len = 0
        

    def insertFront(self, value: int) -> bool:
        if self.len == self.k:
            return False

        n = Node(value)
        if self.len == 0:
            self.front = self.back = n
        else:
            n.next = self.front
            self.front.previous = n
            self.front = n
        
        self.len += 1
        return True
        

    def insertLast(self, value: int) -> bool:
        if self.len == self.k:
            return False

        n = Node(value)
        if self.len == 0:
            self.front = self.back = n
        else:
            n.previous = self.back
            self.back.next = n
            self.back = n

        self.len += 1
        return True

    def deleteFront(self) -> bool:
        if self.len  == 0:
            return False
        if self.len == 1:
            self.front = self.back = None
        else:
            self.front.next.previous = None
            self.front = self.front.next
        
        self.len += -1
        return True

    def deleteLast(self) -> bool:
        if self.len  == 0:
            return False
        if self.len == 1:
            self.front = self.back = None
        else:
            self.back.previous.next = None
            self.back = self.back.previous
        self.len += -1
        return True


    def getFront(self) -> int:
        return -1 if self.len == 0 else self.front.val
        

    def getRear(self) -> int:
        return -1 if self.len == 0 else self.back.val


    def isEmpty(self) -> bool:
        return self.len == 0
        

    def isFull(self) -> bool:
        return self.len == self.k



# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()