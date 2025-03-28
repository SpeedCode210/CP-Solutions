# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

n,k,q = map(int,input().split())

h = [0]*200002
for i in range(n):
    a,b = map(int,input().split())
    h[a] += 1
    h[b+1] -= 1
    
for i in range(1, 200002):
    h[i] += h[i-1]

for i in range(200002):
    h[i] = 1 if h[i] >= k else 0
    
for i in range(1, 200002):
    h[i] += h[i-1]
    
for i in range(q):
    a,b = map(int,input().split())
    print(h[b] - h[a-1])