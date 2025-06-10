# Problem: Design browser history  - https://leetcode.com/problems/design-browser-history/

class Node:
    def __init__(self, val : str, prev = None, nextn = None):
        if prev is None:
            prev = self
        if nextn is None:
            nextn = self
        self.val = val
        self.previous = prev
        self.next = nextn
class BrowserHistory:

    def __init__(self, homepage: str):
        self.graph = Node(homepage)

    def visit(self, url: str) -> None:
        self.graph.next = Node(url, self.graph)
        self.graph = self.graph.next

    def back(self, steps: int) -> str:
        for i in range(steps):
            self.graph = self.graph.previous
        return self.graph.val

    def forward(self, steps: int) -> str:
        for i in range(steps):
            self.graph = self.graph.next
        return self.graph.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)