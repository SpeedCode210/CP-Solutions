# Problem: From adjacency list to adjacency matrix - https://basecamp.eolymp.com/en/problems/3982

n = int(input())
mat = [[0]*n for i in range(n)]
for i in range(n):
    a = [int(x) for x in input().split()]
    for u in range(1, len(a)):
        mat[i][a[u]-1] = 1
for c in mat:
    print(*c)