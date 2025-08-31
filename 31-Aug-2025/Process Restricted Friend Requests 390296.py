# Problem: Process Restricted Friend Requests - https://leetcode.com/problems/process-restricted-friend-requests/

class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        graph = [set() for i in range(n)]

        for x in restrictions:
            graph[x[0]].add(x[1])
            graph[x[1]].add(x[0])

        parent = [i for i in range(n)]
        def get_grp(x):
            h = []
            while parent[x] != x:
                h.append(x)
                x = parent[x]
            for i in h:
                parent[i] = x
            return x

        res = []
        for r in requests:
            x = get_grp(r[0])
            y = get_grp(r[1])
            if x == y:
                res.append(True)
                continue
            if y in graph[x] or x in graph[y]:
                res.append(False)
                continue
            res.append(True)
            for u in graph[x]:
                graph[y].add(get_grp(u))
            parent[x] = y
        return res