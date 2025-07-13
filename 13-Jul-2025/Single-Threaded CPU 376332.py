# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

from heapq import heappop, heappush
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [(tasks[i], i) for i in range(len(tasks))]
        tasks.sort()
        heap = []
        p = 0
        currentTime = -1
        res = []
        while p < len(tasks) or len(heap) > 0:
            while p < len(tasks) and tasks[p][0][0] <= currentTime:
                heappush(heap, (tasks[p][0][1], tasks[p][1]))
                p += 1
            if len(heap) == 0:
                heappush(heap, (tasks[p][0][1], tasks[p][1]))
                currentTime = tasks[p][0][0]
                p += 1
            currentTime += heap[0][0]
            res.append(heap[0][1])
            heappop(heap)
        return res
        
