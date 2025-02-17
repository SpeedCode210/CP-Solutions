# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

from collections import defaultdict

t = int(input())
for i in range(t):
    plus = defaultdict(int)
    moins = defaultdict(int)
    n,m = map(int, input().split())
    X = [[int(x) for x in input().split()] for j in range(n)]
    
    for i in range(n):
        for j in range(m):
            plus[i+j] += X[i][j]
            moins[i-j] += X[i][j]
            
    res = 0
    for i in range(n):
        for j in range(m):
            res = max(res, plus[i+j] + moins[i-j] - X[i][j])
    print(res)
    