# Problem: Time needed to buy tickets - https://leetcode.com/problems/time-needed-to-buy-tickets/

from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        q = deque()
        for i in range(len(tickets)):
            q.appendleft((i, tickets[i]))
        
        while True:
            u = q[-1]
            print(u)
            q.pop()
            if u == (k, 1):
                return res +1
            if u[1] > 1:
                q.appendleft((u[0], u[1] - 1))
            res += 1