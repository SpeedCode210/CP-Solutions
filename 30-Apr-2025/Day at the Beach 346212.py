# Problem: Day at the Beach - https://codeforces.com/problemset/problem/599/C

n = int(input())

h = [int(x) for x in input().split()]

C = []
for i in range(n):
    C.append((h[i], i))
    
C.sort()

res = 0
maxi = -1
for i,y in enumerate(C) :
    maxi = max(y[1], maxi)
    if maxi == i:
        res += 1
        
print(res)