# Problem: Find Consecutive Integers from a Data Stream - https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

from collections import deque

class DataStream:

    def __init__(self, value: int, k: int):
        self.hi = deque()
        self.value = value
        self.count = 0
        self.k = k

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.count += 1
        self.hi.append(num)
        if len(self.hi) > self.k:
            if self.hi[0] == self.value:
                self.count -= 1
            self.hi.popleft()
        return self.k == self.count


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)