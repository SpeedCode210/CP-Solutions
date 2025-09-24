# Problem: Map Sum Pairs - https://leetcode.com/problems/map-sum-pairs/description/

class Node:
    def __init__(self):
        self.ch = [None]*26
        self.val = 0
        self.sum = 0

class MapSum:

    def __init__(self):
        self.root = Node()
        

    def insert(self, key: str, val: int) -> None:
        curr = self.root
        for x in key:
            idx = ord(x) - ord('a')
            if curr.ch[idx] is None:
                curr.ch[idx] = Node()
            curr = curr.ch[idx]
            
        delta = val - curr.val
        curr.val = val
        
        curr = self.root
        for x in key:
            idx = ord(x) - ord('a')
            if curr.ch[idx] is None:
                curr.ch[idx] = Node()
            curr = curr.ch[idx]
            curr.sum += delta
        

    def sum(self, prefix: str) -> int:
        curr = self.root
        for x in prefix:
            idx = ord(x) - ord('a')
            if curr.ch[idx] is None:
                return 0
            curr = curr.ch[idx]
        return curr.sum
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)