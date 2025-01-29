# Problem: Number of Parallelograms - https://codeforces.com/contest/660/problem/D

import math
t = int(input())
a = []
for i in range(0,t):
    a.append([int(x) for x in input().split()])
hi = dict([((0,0),0)])
for i in range(0,t):
    for j in range(i+1, t):
        if a[i][0]-a[j][0] == 0:
            s = (int(math.fabs((a[i][1]-a[j][1]))),-1000000000000)
        else:
            s = (int((a[i][0]-a[j][0])*((a[i][0]-a[j][0])/math.fabs(a[i][0]-a[j][0]))),int((a[i][1]-a[j][1])*((a[i][0]-a[j][0])/math.fabs(a[i][0]-a[j][0]))))
        if s in hi:
            hi[s] = hi[s] + 1
        else :
            hi[s] = 1
res = 0
for x in hi.values():
    res = res + x*(x-1)/2

print(int(res/2))