# Problem: Dijkstra? - https://codeforces.com/problemset/problem/20/C

from heapq import heappush, heappop

n,m = map(int,input().split())

graph = [{} for _ in range(n)]


for _ in range(m):
    a,b,x = map(int,input().split())
    
    if a == b:
        continue
    
    a -= 1
    b -= 1
    
    if b in graph[a]:
        graph[a][b] = min(graph[a][b], x)
    else:
        graph[a][b] = x
        
    a,b = b,a
        
    if b in graph[a]:
        graph[a][b] = min(graph[a][b], x)
    else:
        graph[a][b] = x
        
        
dist = [1000000000000000000]*n
parent = [-1]*n
vis = [False]*n

heap = []

dist[0] = 0

heappush(heap, (0, 0))

while len(heap):
    d, a = heap[0]
    heappop(heap)
    if vis[a]:
        continue
    vis[a] = True
    for x in graph[a]:
        y = graph[a][x]
        if not vis[x] and dist[x] > dist[a] + y:
            dist[x] = dist[a] + y
            parent[x] = a
            heappush(heap, (dist[x], x))
            


if parent[-1] == -1:
    print(-1)
else:
    res = [n]
    while parent[res[-1]-1] != -1:
        res.append(parent[res[-1]-1]+1)
    res.reverse()
    print(*res)