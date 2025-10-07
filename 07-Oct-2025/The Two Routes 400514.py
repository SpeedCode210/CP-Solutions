# Problem: The Two Routes - https://codeforces.com/problemset/problem/601/A

from collections import deque

n,m = map(int,input().split())

graph = [[] for _ in range(n)]

for i in range(m):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

graph_bis = [[j for j in range(n) if j != i and j not in graph[i]] for i in range(n)]

def f(g):
    global n
    bfs = deque()
    bfs.appendleft(0)
    d = [-1]*n
    d[0] = 0
    while len(bfs):
        a = bfs[-1]
        bfs.pop()
        for x in g[a]:
            if d[x] == -1:
                d[x] = d[a] + 1
                bfs.appendleft(x)
                
    return d[-1]

a = [f(graph), f(graph_bis)]
print(-1 if min(a) == -1 else max(a))
        