# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/

from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.last = deque()
        self.arr = [-1]*(10**4 + 1)
        self.power = [-1]*(10**4 + 1)
        self.cap = capacity
        self.works = capacity > 0
        self.counter = 0

    def get(self, key: int) -> int:
        self.counter += 1
        self.last.appendleft((key, self.counter))
        self.power[key] = self.counter
        return self.arr[key]

    def put(self, key: int, value: int) -> None:
        if not(self.works):
            return
        if self.arr[key] != -1:
            self.arr[key] = value
        elif self.cap > 0:
            self.cap -= 1
            self.arr[key] = value
        else:
            while self.arr[self.last[-1][0]] == -1 or self.power[self.last[-1][0]] != self.last[-1][1]:
                self.last.pop()
            self.arr[self.last[-1][0]] = -1
            self.last.pop()
            self.arr[key] = value

        self.counter += 1
        self.last.appendleft((key, self.counter))
        self.power[key] = self.counter


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)