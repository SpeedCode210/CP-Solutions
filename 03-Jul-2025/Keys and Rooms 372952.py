# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        res = [False]*len(rooms)
        res[0] = True
        d = deque()
        d.append(0)
        k = 1
        while len(d):
            a = d[0]
            d.popleft()
            for x in rooms[a]:
                if not res[x]:
                    res[x] = True
                    k += 1
                    d.append(x)
        return k == len(rooms)