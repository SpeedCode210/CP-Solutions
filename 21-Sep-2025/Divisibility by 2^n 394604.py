# Problem: Divisibility by 2^n - https://codeforces.com/contest/1744/problem/D

t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    v2s = []
    v2 = 0
    for i in range(n):
        v2s.append(0)
        while not a[i]&1:
            a[i] >>= 1
            v2 += 1
        X = i+1
        while not X&1:
            X >>= 1
            v2s[-1] += 1
    
    v2s.sort(reverse=True)
    op = 0
    for i in range(n):
        if v2 >= n:
            break
        v2 += v2s[i]
        op += 1
    if v2 >= n:
        print(op)
    else:
        print(-1)
    
    
            
    