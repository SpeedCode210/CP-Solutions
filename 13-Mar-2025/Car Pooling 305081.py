# Problem: Car Pooling - https://leetcode.com/problems/car-pooling/description/

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        x = []
        for t in trips:
            x.append((t[1],1, t[0]))
            x.append((t[2],0, t[0]))
        
        r = 0
        x.sort()
        for u in x:
            if u[1] == 0:
                r-= u[2]
            else:
                r += u[2]
            
            if r > capacity:
                return False
        return True