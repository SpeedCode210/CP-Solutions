# Problem: Regular Graph - https://basecamp.eolymp.com/en/problems/5076

n,m = map(int,input().split())
a = [0]*(n)
for i in range(m):
    x,y = map(int,input().split())
    a[x-1] += 1
    a[y-1] += 1
    
res = True
for i in range(n-1):
    if a[i] != a[i+1]:
        res = False
        break
print("YES" if res else "NO")