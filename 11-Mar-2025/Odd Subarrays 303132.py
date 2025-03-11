# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

t= int(input())
for _ in range(t):
    n = int(input())
    res = 0
    a = [int(x) for x in input().split()]
    i = 0
    while i < n-1:
        if a[i] > a[i+1]:
            i+= 1
            res += 1
        i += 1
    print(res)