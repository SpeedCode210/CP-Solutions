# Problem: Books - https://codeforces.com/contest/279/problem/B

n,t = map(int,input().split())
a = [int(x) for x in input().split()]

p0 = 0
p1 = 0
q = 0
res = 0
while p1 < n:
    if q <= t:
        res = max(res, p1-p0)
        q += a[p1]
        p1 += 1
    else:
        q -= a[p0]
        p0 += 1
if q <= t:
    res = max(res, p1-p0)
print(res)