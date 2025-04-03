# Problem: Sereja and Dima - https://codeforces.com/problemset/problem/381/A

n = int(input())
a = [int(x) for x in input().split()]
A = [0,0]
x = 0
y = -1
for i in range(n):
    if a[x] > a[y]:
        A[i%2] += a[x]
        x += 1
    else:
        A[i%2] += a[y]
        y += -1
print(*A)