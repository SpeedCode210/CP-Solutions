# Problem: Team - https://codeforces.com/contest/231/problem/A

x = 0
t = int(input())
for i in range(t):
    a = [int(y) for y in input().split()]
    if a[0]+a[1]+a[2] > 1:
        x += 1
print(x)