# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

n = int(input())
v = [int(x) for x in input().split()]
c = [0]
d = [0]
for x in v:
    c.append(c[-1] + x)
v.sort()
for x in v:
    d.append(d[-1] + x)
    
m = int(input())

for _ in range(m):
    t,l,r = map(int,input().split())
    if t == 1:
        print(c[r] - c[l-1])
    else:
        print(d[r] - d[l-1])
