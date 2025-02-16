# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

import random

class RandomizedSet:

    def __init__(self):
        self.S = set()
        self.D = dict()
        self.cache = []

    def insert(self, val: int) -> bool:
        if not(val in self.S):
            self.cache.append(val)
            self.D[val] = len(self.cache) - 1
            self.S.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.S:
            self.cache[self.D[val]] = self.cache[-1]
            self.D[self.cache[-1]] = self.D[val]
            self.cache.pop()
            self.S.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return self.cache[random.randint(0, len(self.cache)-1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()