# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

n = int(input())
a = [1]*(n+1)
res = 0
for i in range(2, n+1):
    if a[i] == 3:
        res += 1
    elif a[i] == 1:
        for j in range(i*2, n+1, i):
            a[j] += 1
print(res)
