# Problem: Number of Recent Calls - https://leetcode.com/problems/number-of-recent-calls/

from collections import deque

class RecentCounter:

    def __init__(self):
        self.hi = deque()

    def ping(self, t: int) -> int:
        self.hi.append(t)
        while self.hi[0] < t-3000:
            self.hi.popleft()
        return len(self.hi)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)