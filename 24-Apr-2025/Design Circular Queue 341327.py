# Problem: Design Circular Queue - https://leetcode.com/problems/design-circular-queue/

class Node:
    def __init__(self, v = 0):
        self.val = v
        self.next = None
        self.previous = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.front = None
        self.back = None
        self.k = k
        self.len = 0
        

    def enQueue(self, value: int) -> bool:
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


    def deQueue(self) -> bool:
        if self.len  == 0:
            return False
        if self.len == 1:
            self.front = self.back = None
        else:
            self.back.previous.next = None
            self.back = self.back.previous
        self.len += -1
        return True


    def Front(self) -> int:
        return -1 if self.len == 0 else self.back.val

    def Rear(self) -> int:
        return -1 if self.len == 0 else self.front.val

    def isEmpty(self) -> bool:
        return self.len == 0
        

    def isFull(self) -> bool:
        return self.len == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()