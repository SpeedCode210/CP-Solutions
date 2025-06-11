# Problem: Operations on Graph - https://www.eolymp.com/en/contests/9060/problems/78602

n = int(input())
k = int(input())
graph = [[] for i in range(n)]
for _ in range(k):
    a = [int(x) for x in input().split()]
    if a[0] == 1 :
        graph[a[1]-1].append(a[2])
        graph[a[2]-1].append(a[1])
    else:
        print(" ".join([str(x) for x in graph[a[1]-1]]))