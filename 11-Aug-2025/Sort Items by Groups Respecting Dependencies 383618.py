# Problem: Sort Items by Groups Respecting Dependencies - https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        before = [set() for i in range(n+m)]
        group = [group[i] if group[i] > -1 else m+i for i in range(n)]
        beforeItems = [set(x) for x in beforeItems]
        BFS = [[] for i in range(n+m)]
        graph = [[] for i in range(n)]
        graph2 = [[] for i in range(n+m)]
        
        for i in range(n):
            if len(beforeItems[i])==0:
                BFS[group[i]].append(i) 

            for x in beforeItems[i]:
                graph[x].append(i)

            for x in beforeItems[i]:
                if group[x] != group[i]:
                    before[group[i]].add(group[x])
        for i in range(n+m):
            for x in before[i]:
                graph2[x].append(i)


        bfs = [i for i in range(n+m) if len(before[i]) == 0]
        res = []
        
        while len(bfs):

            x = bfs[-1]
            bfs.pop()
            
            while len(BFS[x]):
                y = BFS[x][-1]
                BFS[x].pop()
                res.append(y)
                for z in graph[y]:
                    beforeItems[z].remove(y)
                    if not len(beforeItems[z]):
                        BFS[group[z]].append(z)

            for y in graph2[x]:
                before[y].remove(x)
                if not len(before[y]):
                    bfs.append(y)
        
        return [] if len(res) != n else res
