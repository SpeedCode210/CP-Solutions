# Problem: Alian Dictionary - https://www.geeksforgeeks.org/problems/alien-dictionary/1

from collections import defaultdict
class Solution:
    def findOrder(words):
        res = []
        graph = defaultdict(lambda : set())
        before = defaultdict(lambda : set())
        h = set()
        for word in words:
            for i in word:
                h.add(i)
            
        for i in range(len(words)-1):
            k = True
            for j in range(min(len(words[i]), len(words[i+1]))):
                if words[i][j] ==  words[i+1][j]:
                    continue
                k = False
                graph[words[i][j]].add(words[i+1][j])
                before[words[i+1][j]].add(words[i][j])
                break
                
            if k and len(words[i+1]) < len(words[i]):
                return ""
                
                
        bfs = [x for x in h if len(before[x]) == 0]

        while len(bfs):
            x = bfs[-1]
            bfs.pop()
            res.append(x)
            for y in graph[x]:
                before[y].remove(x)
                if len(before[y]) == 0:
                    bfs.append(y)
                    
        
        return "".join(res) if len(res) == len(h) else ""

