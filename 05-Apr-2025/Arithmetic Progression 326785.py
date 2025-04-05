# Problem: Arithmetic Progression - https://codeforces.com/problemset/problem/382/C

from collections import defaultdict
n = int(input())
S = set()
u = defaultdict(int)
 
a = [int(x) for x in input().split()]
a.sort()
m = 1000000000
M = 0
for i in range(1, n):
    s = a[i] - a[i-1]
    S.add(s)
    u[s] += 1
    m = min(s, m)
    M = max(s, M)
    
if n == 1:
    print(-1)
elif n==2:
    if a[1]-a[0] == 0:
        print(1)
        print(a[0])
    elif (a[1]-a[0])%2 == 1:
        print(2)
        print(*sorted([2*a[1]-a[0],2*a[0]-a[1]]))
    else:
        print(3)
        print(*sorted([2*a[0]-a[1], (a[0]+a[1])//2,2*a[1]-a[0]]))
 
elif len(S) > 2 or (len(S) == 2 and (2*m != M or u[M] != 1)):
    print(0)
elif len(S) == 1:
    x = S.pop()
    if x == 0:
        print(1)
        print(a[0])
    else:
        print(2)
        print(*sorted([a[0]-x, a[-1]+x]))
else:
    for i in range(1, n):
        if a[i] - a[i-1] == M:
            print(1)
            print((a[i] + a[i-1])//2)
