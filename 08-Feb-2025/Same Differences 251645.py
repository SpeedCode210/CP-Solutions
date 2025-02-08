# Problem: Same Differences - https://codeforces.com/problemset/problem/1520/D

from collections import defaultdict 
t = int(input())
for i in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    d = defaultdict(int)
    for i in range(n):
        d[a[i]-i] += 1
    res = 0
    for x in d:
        res += d[x]*(d[x]-1)//2
    print(res)