# Problem: Task Scheduler - https://leetcode.com/problems/task-scheduler/

from collections import Counter, defaultdict
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        C = Counter(tasks)
        last = defaultdict(lambda : -1000)
        res = 0
        X = len(tasks)
        i = 0
        while X > 0:
            for cp in sorted([(C[x], x) for x in C], reverse=True):
                c = cp[1]
                if C[c] > 0 and i - last[c] > n:
                    last[c] = i
                    X -= 1
                    C[c] -= 1
                    i += 1
                    res += 1
                    break
            else:
                res += 1
                i += 1
        return res