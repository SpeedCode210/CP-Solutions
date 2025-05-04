# Problem: Min Stack - https://leetcode.com/problems/min-stack/

class Node:
    def __init__(self, x):
        self.next = None
        self.val = x
        self.mini = x
class MinStack:

    def __init__(self):
        self.st = None
    
    def push(self, val: int) -> None:
        n = Node(val)
        if self.st != None:
            n.mini = min(n.mini, self.st.mini)
        n.next = self.st
        self.st = n

    def pop(self) -> None:
        self.st = self.st.next

    def top(self) -> int:
        return self.st.val

    def getMin(self) -> int:
        return self.st.mini


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()